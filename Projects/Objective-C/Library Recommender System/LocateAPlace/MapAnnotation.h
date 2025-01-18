//
//  MapAnnotation.h
//  LocateAPlace
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <Corelocation/CoreLocation.h>
#import <MapKit/MapKit.h>


@interface MapAnnotation : NSObject <MKAnnotation> {
		NSString *title;
		CLLocationCoordinate2D coordinate;
}

@property (nonatomic, readwrite) CLLocationCoordinate2D coordinate;
@property (nonatomic, copy) NSString *title;

- (id) initWithCoordinate: (CLLocationCoordinate2D) c title: (NSString *) t;

@end
