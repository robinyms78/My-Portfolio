//
//  LocateAPlaceAppDelegate.h
//  LocateAPlace
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>

@class LocalMapViewController;

@interface LocateAPlaceAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
	LocalMapViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@end

