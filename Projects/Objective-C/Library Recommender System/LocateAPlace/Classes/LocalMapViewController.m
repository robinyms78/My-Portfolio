//
//  LocalMapViewController.m
//  LocateAPlace
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import "LocalMapViewController.h"

@implementation LocalMapViewController

- (BOOL) textFieldShouldReturn: (UITextField *) tf
	{
		//	retrieve geocode
		NSString *urlLocation = [NSString stringWithFormat:@"http://maps.google.com/maps/geo?q=%@&output=csv",
								[locationTitleField.text stringByAddingPercentEscapesUsingEncoding: NSUTF8StringEncoding]];
								 NSString *locationString = [NSString stringWithContentsOfURL:[NSURL URLWithString: urlLocation]
								 encoding: NSASCIIStringEncoding
								 error: nil];
		
		NSArray *itemsLocation = [locationString componentsSeparatedByString:@","];
		
		double latitude = 0.0;
		double longitude = 0.0;

		if ([itemsLocation count] >= 4 && [[itemsLocation objectAtIndex: 0] isEqualToString:@"200"]) {
			latitude = [[itemsLocation objectAtIndex: 2] doubleValue];
			longitude = [[itemsLocation objectAtIndex: 3] doubleValue];
		}
		else {
			NSLog(@"Cannot locate the location");
		}

		CLLocationCoordinate2D newCoordinate;
		newCoordinate.latitude = latitude;
		newCoordinate.longitude = longitude;
	
		//Create an MapAnnotation object and put it on the MapView
		
		MapAnnotation *ma = [[MapAnnotation alloc]
							 initWithCoordinate:newCoordinate title: [locationTitleField text]];  
							 [mapView addAnnotation:ma];
							 [mapView setCenterCoordinate: newCoordinate animated: YES];
		
		// Structure to define areas spanned by a map region MKCoordinateRegion region;
		
		MKCoordinateRegion region;
		
		region.center = newCoordinate;
		
		// Define the distance (in degrees) to be display
		
		region.span.latitudeDelta = .005;
		region.span.longitudeDelta = .005;
		
		[mapView setRegion: region animated: TRUE];
		
		[ma release];
		[tf resignFirstResponder];
		return YES;
	}

- (id) initWithNibName: (NSString *) nibNameOrNil bundle: (NSBundle *) nibBundleOrNil {
		self = [super initWithNibName:nibNameOrNil
		bundle:nibBundleOrNil];
		if (self) {
		}
		
		return self;

	}

- (void) didReceiveMemoryWarning {
	[super didReceiveMemoryWarning];

}

- (void) viewDidUnload {
	[super viewDidUnload];
	[mapView release];
	[locationTitleField release];
}

- (void) dealloc {
	[mapView release];
	[locationTitleField release];
    [super dealloc];
}

@end
