//
//  LocationManagerAppDelegate.h
//  LocationManager
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>

@class LocationViewController;

@interface LocationManagerAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
	LocationViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@end

