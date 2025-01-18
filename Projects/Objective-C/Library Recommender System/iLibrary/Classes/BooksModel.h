//
//  BooksModel.h
//  Modules
//
//  Created by student on 6/2/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface BooksModel : NSObject {
	NSString *bookName;
	NSDate *dueDate;
	NSDate *issueDate;
	NSString *callNumber;
}
@property(nonatomic,copy) NSString *bookName;
@property(nonatomic,copy) NSDate *dueDate;
@property(nonatomic,copy) NSDate *issueDate;
@property(nonatomic,copy) NSString *callNumber;
@end
