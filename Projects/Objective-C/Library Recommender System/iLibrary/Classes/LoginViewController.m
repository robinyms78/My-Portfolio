//
//  LoginViewController.m
//  Login
//
//  Created by Mok Hei Chee on 5/19/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "LoginViewController.h"
#import "LoginModel.h"
#import "MyAccountModel.h"
#import "MyAccountViewController.h"
#import "MyAccountSub1ViewController.h"
#import "BooksModel.h"

@implementation LoginViewController
@synthesize userID, password,booksModel;


// The designated initializer.  Override if you create the controller programmatically and want to perform customization that is not appropriate for viewDidLoad.
/*
- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil {
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization.
    }
    return self;
}
*/


// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad {
    [super viewDidLoad];
	loginModel = [[LoginModel alloc] init];
	self.booksModel = [[NSMutableArray alloc] init];
	userID.delegate = self;
	password.delegate = self;
}

-(void)textFieldShouldReturn:(UITextField *)textField{
	[userID resignFirstResponder];
	[password resignFirstResponder];
	}

-(IBAction) login{
	[userID resignFirstResponder];
	[password resignFirstResponder];
	NSString *name = userID.text;
	NSString *pass = password.text;
	NSLog(@"UserName is %@ and password is %@",name,pass);
	BOOL result = [loginModel verifyUser:name andPassword:pass];
	if(!result){
		[self printMessage:@"Incorrect userID or password!"];
	} else {
		//[self printMessage:@"Welcome to the Library application!"];
		MyAccountViewController *accountViewController= [[MyAccountViewController alloc] initWithNibName:@"MyAccountViewController" bundle:[NSBundle mainBundle]];
		[accountViewController setUserId:userID.text];
		// Query the Webservice and Populate the Books Model Array with teh list of Books which the user has
		/*Adding 2 Book details */
		
		BooksModel *book1 =[[BooksModel alloc] init];
		
		book1.callNumber=@"110000";
		book1.bookName=@"Introduction to Expert Systems";
		NSDateComponents *components = [[NSDateComponents alloc] init];
		[components setWeekday:12]; // Monday
		[components setMonth:5]; // May
		[components setYear:2011];
		
		NSDateComponents *components2 = [[NSDateComponents alloc] init];
		[components setWeekday:02]; // Monday
		[components setMonth:6]; // May
		[components setYear:2011];
		
		NSCalendar *gregorian = [[NSCalendar alloc]
								 initWithCalendarIdentifier:NSGregorianCalendar];
		//NSDate *date = [gregorian dateFromComponents:components];
		
		
		
		book1.dueDate=[gregorian dateFromComponents:components];
		book1.issueDate=[gregorian dateFromComponents:components2];
		BooksModel *book2 =[[BooksModel alloc] init];
		book2.callNumber=@"22200";
		book2.bookName=@"Introduction to Fuzzy Systems";
		book2.dueDate=[gregorian dateFromComponents:components];
		book2.issueDate=[gregorian dateFromComponents:components2];
		
		[self.booksModel addObject:book1];		
		[self.booksModel addObject:book2];	
		
		/*End of Hard Coding*/
		
			
		[accountViewController setBooksModel:self.booksModel];
		
		[[self view] addSubview:accountViewController.view];
		//[accountViewController autorelease];
	}

	
	
}
-(void) printMessage:(NSString *)name{
	UIAlertView *alertPopUp = [[UIAlertView alloc]
							   initWithTitle:@"Alert"
							   message:name
							   delegate:nil
							   cancelButtonTitle:@"OK"
							   otherButtonTitles:nil];
	[alertPopUp show];
	NSLog(@"The message is %@",name);
}



// Override to allow orientations other than the default portrait orientation.
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
    // Return YES for supported orientations.
    //return (interfaceOrientation == UIInterfaceOrientationPortrait);
	return YES;
}


- (void)didReceiveMemoryWarning {
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc. that aren't in use.
}

- (void)viewDidUnload {
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}


- (void)dealloc {
	[booksModel release];
    [super dealloc];
}


@end
