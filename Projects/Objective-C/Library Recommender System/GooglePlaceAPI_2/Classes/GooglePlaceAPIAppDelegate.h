//
//  GooglePlaceAPIAppDelegate.h
//  GooglePlaceAPI
//
//  Created by Robin Yap on 5/27/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>

@class GooglePlaceAPIAppDelegate;

@interface GooglePlaceAPIAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@end

