//
//  Constants.h
//  Concierge
//
//  Created by Sam Zeckendorf on 9/28/12.
//  Copyright (c) 2012 hi ku llc. All rights reserved.
//

#ifndef Concierge_Constants_h
#define Concierge_Constants_h

#define CGLOG(format, ...)                       NSLog(@"%d,%s,"format,__LINE__,__FUNCTION__,##__VA_ARGS__);
#define CGLOG_CALLED                             CGLOG(@"called")
#define SERVER_URL                               @"http://localhost:8000/"
#define QUESTION_API_EXT                         @"api/v1/restaurant/?format=json"
#endif
