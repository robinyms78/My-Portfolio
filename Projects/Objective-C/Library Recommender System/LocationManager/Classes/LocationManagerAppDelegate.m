//
//  LocationManagerAppDelegate.m
//  LocationManager
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import "LocationManagerAppDelegate.h"
#import "LocationViewController.h"

@implementation LocationManagerAppDelegate

@synthesize window;


#pragma mark -
#pragma mark Application lifecycle

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    
    
	viewController = [[LocationViewController alloc] 
			initWithNibName: @"LocationViewController"
			bundle: [NSBundle mainBundle]];
	[self.window addSubview:viewController.view];
    
    [self.window makeKeyAndVisible];
    
    return YES;
}

@end

