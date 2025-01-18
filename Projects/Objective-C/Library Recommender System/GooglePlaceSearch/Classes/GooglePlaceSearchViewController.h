//
//  GooglePlaceSearchViewController.h
//  GooglePlaceSearch
//
//  Created by Robin Yap on 6/5/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface GooglePlaceSearchViewController: UIViewController {
	UILabel *latitude;
	UILabel *longitude;
	UIActivityIndicatorView *activityIndicatorView;
	NSURLConnection *conn;
	NSMutableData *buffer;	
}

@property (nonatomic, retain) IBOutlet UILabel *latitude;
@property (nonatomic, retain) IBOutlet UILabel *longitude;
@property (nonatomic, retain) IBOutlet UIActivityIndicatorView *activityIndicatorView;
@property (nonatomic, retain) NSMutableData *buffer;

-(IBAction) lookup;

@end