//
//  GooglePlaceSearchAppDelegate.h
//  GooglePlaceSearch
//
//  Created by Robin Yap on 6/5/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>

@class GooglePlaceSearchViewController;

@interface GooglePlaceSearchAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    GooglePlaceSearchViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet GooglePlaceSearchViewController *viewController;

@end

