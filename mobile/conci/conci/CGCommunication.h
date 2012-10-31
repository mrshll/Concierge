#import <Foundation/Foundation.h>
#import "ASIHTTPRequest.h"
#import "ASIFormDataRequest.h"

/***********************************************************
 *** Communication Class to encapsulate                  ***
 *** all the boring HTTP request stuff in ASIHTTPRequest ***
 ***********************************************************/

@interface CGCommunication : NSObject

@property (strong, nonatomic) id delegate;

- (CGCommunication *)initWithDelegate:(id)delegate;
- (void)postWithOptions:(NSDictionary*)options toUrl:(NSString*)url;
- (void)getUrl:(NSURL *)url;
- (void)getUrlSync:(NSURL *)url;
- (void)getUrl:(NSURL *)url withCookies:(NSMutableArray*)cookies;

@end

// Protocol for the authorization delegate
@protocol CommDelegate <NSObject>
@required
- (void)requestFinished:(ASIHTTPRequest *)request;
- (void)requestFailed:(ASIHTTPRequest *)request;

@property (strong, nonatomic) CGCommunication *communicator;
@end