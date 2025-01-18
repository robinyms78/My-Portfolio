//
//  LocationViewController.m
//  LocationManager
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import "LocationViewController.h"

@implementation LocationViewController

- (void) updateLocation: (NSString *) locationDesc{
	NSMutableString *newMessage = [[NSMutableString alloc] initWithCapacity:100];
	[newMessage appendString:
	[NSString stringWithFormat:@"Update #:%i\n", noUpdates]];
	[newMessage appendString: locationDesc];
	[newMessage appendString: @"\n"];
	[newMessage appendString: [textView text]];
	textView.text = newMessage;
	[newMessage release];

}

- (void) locationManager: (CLLocationManager *) manager
	 didUpdateToLocation: (CLLocation *) newLocation
			fromLocation: (CLLocation *) oldLocation

{
	NSLog(@"%@", newLocation);
	noUpdates++;
	if(noUpdates >= 50) {
		[locationManager stopUpdatingLocation];
		textView.text = @"Location Manager stop running ...";
	}
		[self updateLocation: [newLocation description]];

}

- (void) locationManager: (CLLocationManager *) manager
			didFailWithError:(NSError *) error
{
			NSLog(@"Could not locate location:%@", error);
}
	
- (id) initWithNibName: (NSString *) nibNameOrNil
				bundle: (NSBundle *) nibBundleOrNil {
			self = [super initWithNibName: nibNameOrNil
				    bundle:nibBundleOrNil];
			if (self) {
				locationManager = [[CLLocationManager alloc] init];
				[locationManager setDelegate: self];
				[locationManager startUpdatingLocation];
			}
			return self;

}
				
// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad {
    [super viewDidLoad];
	textView.text = @"Location Manager start running...";
}

- (void)viewDidUnload {
    [super viewDidUnload];
	[textView release];
}

- (void)dealloc {
    [super dealloc];
	[textView release];
	[locationManager release];
}

@end
