//
//  LocalMapViewController.h
//  LocateAPlace
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MapKit/MapKit.h>
#import "MapAnnotation.h"

@interface LocalMapViewController : UIViewController {
		IBOutlet MKMapView *mapView;
		IBOutlet UITextField *locationTitleField;

}

@end
