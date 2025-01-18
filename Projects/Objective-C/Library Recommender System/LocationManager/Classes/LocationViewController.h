//
//  LocationViewController.h
//  LocationManager
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <CoreLocation/CoreLocation.h>

@interface LocationViewController : UIViewController <CLLocationManagerDelegate> {
		IBOutlet UITextView *textView;
	CLLocationManager *locationManager;
	NSUInteger noUpdates;

}

@end
