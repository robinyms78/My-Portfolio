//
//  ModulesViewController.h
//  Modules
//
//  Created by Mok Hei Chee on 5/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class ModulesSub1ViewController;
@class ModulesSub2ViewController;
@class ModulesSub3ViewController;
@class ModulesSub4ViewController;
@class ModulesModel;
@class LoginViewController;
@class LoginModel;
@class MyAccountModel;
@class MyAccountViewController;
@class MyAccountSub1ViewController;
@class MyAccountSub2ViewController;
@class MyAccountSub3ViewController;

@interface ModulesViewController : UITableViewController {
	ModulesModel *modulesModel;
	ModulesSub1ViewController *sub1ViewController;
	ModulesSub2ViewController *sub2ViewController;
	ModulesSub3ViewController *sub3ViewController;
	ModulesSub4ViewController *sub4ViewController;
	LoginViewController *loginViewController;
	LoginModel *loginModel;
	MyAccountModel *myAccountModel;
	MyAccountViewController *myAccountViewController;
	MyAccountSub1ViewController *accountsub1ViewController;
	MyAccountSub2ViewController *accountsub2ViewController;
	MyAccountSub3ViewController *accountsub3ViewController;
}

@property (nonatomic,retain)ModulesModel *modulesModel;
@property (nonatomic,retain)ModulesSub1ViewController *sub1ViewController;
@property (nonatomic,retain)ModulesSub2ViewController *sub2ViewController;
@property (nonatomic,retain)ModulesSub3ViewController *sub3ViewController;
@property (nonatomic,retain)ModulesSub4ViewController *sub4ViewController;
@property (nonatomic,retain)LoginViewController *loginViewController;
@property (nonatomic,retain)LoginModel *loginModel;
@property (nonatomic,retain)MyAccountModel *myAccountModel;
@property (nonatomic,retain)MyAccountViewController *myAccountViewController;
@property (nonatomic,retain)MyAccountSub1ViewController *accountsub1ViewController;
@property (nonatomic,retain)MyAccountSub2ViewController *accountsub2ViewController;
@property (nonatomic,retain)MyAccountSub3ViewController *accountsub3ViewController;


@end
