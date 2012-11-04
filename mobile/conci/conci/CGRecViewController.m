//
//  CGFirstViewController.m
//  conci
//
//  Created by Marshall Moutenot on 10/27/12.
//  Copyright (c) 2012 Marshall Moutenot. All rights reserved.
//

#import "Constants.h"
#import "CGCommunication.h"
#import "CGRecViewController.h"
#import "SBJson.h"

@interface CGRecViewController ()

@property (weak, nonatomic) IBOutlet UILabel *recText;

@end

@implementation CGRecViewController

@synthesize communicator;

- (void)viewDidLoad
{
    
  CLController = [[CGCoreLocationController alloc] init];
  CLController.dgate = self;
  [CLController.locMgr startUpdatingLocation];
    
    
  [super viewDidLoad];
  communicator = [[CGCommunication alloc] initWithDelegate:self];
  
  // start asking the server api for a list of recs
  NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"%@%@", SERVER_URL, GET_REC_EXT]];
  
  CGLOG(@"Making request at URL:%@", url)
  [communicator getUrl:url];
}



- (void)locationUpdate:(CLLocation *)location {
	locLabel.text = [location description];
}

- (void)locationError:(NSError *)error {
	locLabel.text = [error description];
}

- (void)didReceiveMemoryWarning
{
  [super didReceiveMemoryWarning];
  // Dispose of any resources that can be recreated.
}

- (void) requestFinished:(ASIHTTPRequest *)request {
  NSString *responseString = [request responseString];
  CGLOG(@"%@",responseString);
//  NSArray *responseArray = [[responseString JSONValue] objectForKey:@"objects"];
//  
//  NSDictionary *firstRestaurant = [responseArray objectAtIndex:7];
//  NSString *title= [firstRestaurant objectForKey:@"title"];
//  // this is just for the prototype to get the first value
//  [self.recText setText:title];
  [self.recText setText:responseString];
}

- (void) requestFailed:(ASIHTTPRequest *)request {
  CGLOG(@"REQUEST FAILED");
  
}

@end
