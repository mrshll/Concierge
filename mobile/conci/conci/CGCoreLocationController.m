//
//  CGCoreLocationController.m
//  conci
//
//  Created by Albert Nichols on 11/1/12.
//  Copyright (c) 2012 Marshall Moutenot. All rights reserved.
//

#import "CGCoreLocationController.h"
#import "CGCommunication.h"

@implementation CGCoreLocationController

@synthesize locMgr, dgate;

- (id)init {
	//self = [super init];
    
	if(self != nil) {
		self.locMgr = [[CLLocationManager alloc] init];
        // Create new instance of locMgr
		self.locMgr.delegate = self; // Set the delegate as self.
	}
    
	return self;
}

- (void)locationManager:(CLLocationManager *)manager didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation *)oldLocation {
	if([self.dgate conformsToProtocol:@protocol(CoreLocationControllerDelegate)]) {  // Check if the class assigning itself as the delegate conforms to our protocol.  If not, the message will go nowhere.  Not good.
		[self.dgate locationUpdate:newLocation];
	}
}

- (void)locationManager:(CLLocationManager *)manager didFailWithError:(NSError *)error {
	if([self.dgate conformsToProtocol:@protocol(CoreLocationControllerDelegate)]) {  // Check if the class assigning itself as the delegate conforms to our protocol.  If not, the message will go nowhere.  Not good.
		[self.dgate locationError:error];
	}
}
//Not needed?
/*- (void)dealloc {
	[self.locMgr release];
	[super dealloc];
}*/

@end


