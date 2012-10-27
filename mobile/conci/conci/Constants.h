//
//  Constants.h
//  LoopIt
//
//  Created by Sam Zeckendorf on 9/28/12.
//  Copyright (c) 2012 hi ku llc. All rights reserved.
//

#ifndef LoopIt_Constants_h
#define LoopIt_Constants_h

#define LTLOG(format, ...)                       NSLog(@"%d,%s,"format,__LINE__,__FUNCTION__,##__VA_ARGS__);
#define LTLOG_CALLED                             LTLOG(@"called")
#define SERVER_URL                               @"http://dev.nevershopalone.com/"
#define FB_EXT                                   @"facebook_auth/"
#define QUESTION_API_EXT                         @"api/v1/question/"
#define QUESTION_FETCH_API_EXT                   @"api/v1/question/?format=json&asker__username="
#define USER_API_EXT                             @"api/v1/user/?format=json/"
#endif
