#import "CGCommunication.h"
#import "SBJson.h"
#import "Constants.h"

@implementation CGCommunication
    
@synthesize delegate = _delegate;

- (CGCommunication *)initWithDelegate:(id)delegate
{
  if((self = [super init]))
  {
    self.delegate = delegate;
  }
  return self;
}

- (void)postWithOptions:(NSDictionary *)options toUrl:(NSString *)url{
  

  ASIFormDataRequest *request = [[ASIFormDataRequest alloc] initWithURL:[NSURL URLWithString:url]];
  
  for (NSString* key in [options allKeys]) {
    [request setPostValue:[options valueForKey:key] forKey:key];
    
  }
  
  [request setDelegate:self.delegate];
  [request setTimeOutSeconds:120];
  [request startAsynchronous];

}

- (void)getUrl:(NSURL *)url
{
  ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
  [request setDelegate:self.delegate];
  [request startAsynchronous];
}

- (void)getUrlSync:(NSURL *)url
{
  ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
  [request setDelegate:self.delegate];
  [request startSynchronous];
}

- (void)getUrl:(NSURL *)url withCookies:(NSMutableArray *)cookies
{
  ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
  [request setDelegate:self.delegate];
  [request setRequestCookies:cookies];
  [request startAsynchronous];
}

/* EXAMPLES OF DELEGATE REQUEST HANDLERS

- (void)requestFinished:(ASIHTTPRequest *)request
{
  NSString *responseString = [request responseString];
  NSDictionary *responseDict = [responseString JSONValue];
  LTLOG(@"Response: %@",responseString);
  
  NSData* responseData = [request responseData];
  //Do stuff here with cookie etc.
  
  //Do stuff here with NSDictionary
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
  NSError *error = [request error];
  LTLOG(@"Error: %@",error);
}
 */


@end
