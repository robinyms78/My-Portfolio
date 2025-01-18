//
//  MyAccountModel.m
//  MyAccount
//
//  Created by Mok Hei Chee on 5/31/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "MyAccountModel.h"



@implementation MyAccountModel

@synthesize arrayData;

-(id)init{
	[super init];
	arrayData = [[NSMutableArray alloc]
				 initWithObjects:@"Account Details", @"Borrow Book", @"Set Alerts",@"Pay Fine", nil];
	return self;
}

@end
