//
//  RootViewController.h
//  MyAccount
//
//  Created by Mok Hei Chee on 5/31/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>
# import <EventKit/EventKit.h>
#import <EventKitUI/EventKitUI.h>

@class MyAccountModel;
@class MyAccountSub1ViewController;
@class MyAccountSub2ViewController;
@class MyAccountSub3ViewController;
@class BooksModel;

@interface MyAccountViewController : UITableViewController {
	MyAccountModel *myAccountModel;
	MyAccountSub1ViewController *sub1ViewController;
	MyAccountSub2ViewController *sub2ViewController;
	MyAccountSub3ViewController *sub3ViewController;
	NSString *userId;
	NSMutableArray *booksModel;
	
	NSArray *eventArray;
	EKEventStore *eventStore;

}
@property(nonatomic,retain) NSArray *eventArray;
@property(nonatomic,retain) EKEventStore *eventStore;
@property(nonatomic,retain)NSMutableArray *booksModel;
@property(nonatomic,retain)NSString *userId;
@property(nonatomic,retain)MyAccountModel *myAccountModel;
@property(nonatomic,retain)MyAccountSub1ViewController *sub1ViewController;
@property(nonatomic,retain)MyAccountSub2ViewController *sub2ViewController;
@property(nonatomic,retain)MyAccountSub3ViewController *sub3ViewController;

@end
