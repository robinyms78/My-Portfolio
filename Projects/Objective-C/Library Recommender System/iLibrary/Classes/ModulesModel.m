//
//  ModulesModel.m
//  Modules
//
//  Created by Mok Hei Chee on 5/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "ModulesModel.h"


@implementation ModulesModel

@synthesize arrayData;

-(id) init {
	[super init];
	arrayData = [[NSMutableArray alloc] initWithObjects:@"Catalogue Search",
														@"My Account",
														@"Find Library",nil];
	return self;
}

@end
