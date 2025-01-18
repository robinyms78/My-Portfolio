//
//  GooglePlaceAPIViewController.h
//  GooglePlaceAPI
//
//  Created by Robin Yap on 5/27/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>

@class GooglePlaceAPIViewController;

@interface GooglePlaceAPIViewController: UIViewController {
	UILabel *nearestlibrary;
	UITextField *searchlatlong;
	UIActivityIndicatorView *activityIndicatorView;
	bool libraryfound;
	
	NSURLConnection *conn;
	NSMutableData *buffer;	
}

@property (nonatomic, retain) IBOutlet UILabel *nearestlibrary;
@property (nonatomic, retain) IBOutlet UITextField *searchlatlong;
@property (nonatomic, retain) IBOutlet UIActivityIndicatorView *activityIndicatorView;
@property (nonatomic, retain) NSMutableData *buffer;

-(IBAction) search;
-(void) processResponse:(NSMutableData *) data;

@end
