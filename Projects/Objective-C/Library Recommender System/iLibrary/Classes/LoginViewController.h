//
//  LoginViewController.h
//  Login
//
//  Created by Mok Hei Chee on 5/19/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class LoginModel;
@class MyAccountModel;
@class MyAccountViewController;
@class MyAccountSub1ViewController;

@interface LoginViewController : UIViewController <UITextFieldDelegate> {
	UITextField *userID;
	UITextField *password;
	LoginModel *loginModel;
	NSMutableArray *booksModel;
}

@property(nonatomic,retain)IBOutlet UITextField *userID;
@property(nonatomic,retain)IBOutlet UITextField *password;
@property(nonatomic,retain)NSMutableArray *booksModel;

-(IBAction) login;
-(void) printMessage:(NSString *)name;
-(void)textFieldShouldReturn:(UITextField *)textField;

@end
