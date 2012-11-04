//
//  CGFirstViewController.h
//  conci
//
//  Created by Marshall Moutenot on 10/27/12.
//  Copyright (c) 2012 Marshall Moutenot. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "CGCommunication.h"
#import "CGCoreLocationController.h"

@interface CGRecViewController: UIViewController <CommDelegate,CoreLocationControllerDelegate>{
	CGCoreLocationController *CLController;
	IBOutlet UILabel *locLabel;
}
@property (nonatomic, retain) CGCoreLocationController *CLController;


@end
