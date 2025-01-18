//
//  BooksModel.m
//  Modules
//
//  Created by student on 6/2/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "BooksModel.h"


@implementation BooksModel
@synthesize bookName, dueDate,issueDate,callNumber;
- (id) init {
	self.bookName = [[NSString alloc] init];
	self.dueDate = [[NSDate alloc] init];
	self.issueDate = [[NSDate alloc] init];
	self.callNumber =[[NSString alloc] init];
	return self;
}

- (void) dealloc {
	[bookName release];
	[dueDate release];
	[issueDate release];
	[callNumber release];
	[super dealloc];
}

@end
