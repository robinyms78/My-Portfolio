//
//  MapAnnotation.m
//  LocateAPlace
//
//  Created by Robin Yap on 5/26/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import "MapAnnotation.h"

@implementation MapAnnotation

@synthesize coordinate, title;

- (id) initWithCoordinate:(CLLocationCoordinate2D)c title: (NSString *) t { 
				[super init];
				coordinate = c;	
				[self setTitle: t];
				return self;
}

-(void) dealloc	{
	[title release];
	[super dealloc];
}
	
@end
