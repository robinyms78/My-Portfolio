//
//  ModulesViewController.m
//  Modules
//
//  Created by Mok Hei Chee on 5/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "ModulesViewController.h"
#import "ModulesModel.h";
#import "ModulesSub1ViewController.h";
#import "ModulesSub2ViewController.h";
#import "ModulesSub3ViewController.h";
#import "ModulesSub4ViewController.h";
#import "LoginModel.h";
#import "LoginViewController.h";
#import "MyAccountModel.h";
#import "MyAccountViewController.h";
#import "MyAccountSub1ViewController.h";
#import "MyAccountSub2ViewController.h";
#import "MyAccountSub3ViewController.h";


@implementation ModulesViewController

@synthesize modulesModel, sub1ViewController, sub2ViewController, sub3ViewController, sub4ViewController, loginModel, loginViewController,
			myAccountModel, myAccountViewController, accountsub1ViewController, accountsub2ViewController, accountsub3ViewController;


#pragma mark -
#pragma mark View lifecycle


- (void)viewDidLoad {
    [super viewDidLoad];

    // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
    // self.navigationItem.rightBarButtonItem = self.editButtonItem;
	self.title = @"iLibrary";
	modulesModel = [[ModulesModel alloc] init];
}


/*
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
}
*/
/*
- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
}
*/
/*
- (void)viewWillDisappear:(BOOL)animated {
	[super viewWillDisappear:animated];
}
*/
/*
- (void)viewDidDisappear:(BOOL)animated {
	[super viewDidDisappear:animated];
}
*/

/*
 // Override to allow orientations other than the default portrait orientation.
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
	// Return YES for supported orientations.
	return (interfaceOrientation == UIInterfaceOrientationPortrait);
}
 */


#pragma mark -
#pragma mark Table view data source

// Customize the number of sections in the table view.
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return 1;
}


// Customize the number of rows in the table view.
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return modulesModel.arrayData.count;
	// NSLog(@"The number of rows of data is ",modulesModel.arrayData.count);
}


// Customize the appearance of table view cells.
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    
    static NSString *CellIdentifier = @"Cell";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier] autorelease];
    }
    
	// Configure the cell.
	NSUInteger row = indexPath.row;
	cell.textLabel.text = [modulesModel.arrayData objectAtIndex:row];

    return cell;
}


/*
// Override to support conditional editing of the table view.
- (BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath {
    // Return NO if you do not want the specified item to be editable.
    return YES;
}
*/


/*
// Override to support editing the table view.
- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath {
    
    if (editingStyle == UITableViewCellEditingStyleDelete) {
        // Delete the row from the data source.
        [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath] withRowAnimation:UITableViewRowAnimationFade];
    }   
    else if (editingStyle == UITableViewCellEditingStyleInsert) {
        // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view.
    }   
}
*/


/*
// Override to support rearranging the table view.
- (void)tableView:(UITableView *)tableView moveRowAtIndexPath:(NSIndexPath *)fromIndexPath toIndexPath:(NSIndexPath *)toIndexPath {
}
*/


/*
// Override to support conditional rearranging of the table view.
- (BOOL)tableView:(UITableView *)tableView canMoveRowAtIndexPath:(NSIndexPath *)indexPath {
    // Return NO if you do not want the item to be re-orderable.
    return YES;
}
*/


#pragma mark -
#pragma mark Table view delegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    
	/*
	 <#DetailViewController#> *detailViewController = [[<#DetailViewController#> alloc] initWithNibName:@"<#Nib name#>" bundle:nil];
     // ...
     // Pass the selected object to the new view controller.
	 [self.navigationController pushViewController:detailViewController animated:YES];
	 [detailViewController release];
	 */
	
	if (self.sub1ViewController == nil){
		self.sub1ViewController = [[ModulesSub1ViewController alloc]
								   initWithNibName:@"ModulesSub1ViewController"
								   bundle:[NSBundle mainBundle]];
		self.sub1ViewController.title = @"Catalogue Search";
	}
	
	if (self.loginViewController == nil){
		self.loginViewController = [[LoginViewController alloc]
								   initWithNibName:@"LoginViewController"
								   bundle:[NSBundle mainBundle]];
		self.loginViewController.title = @"My Account";
	}
	
	/*if (self.sub3ViewController == nil){
		self.sub3ViewController = [[ModulesSub3ViewController alloc]
								   initWithNibName:@"ModulesSub3ViewController"
								   bundle:[NSBundle mainBundle]];
		self.sub3ViewController.title = @"Borrow Books";
	}*/
	
	if (self.sub4ViewController == nil){
		self.sub4ViewController = [[ModulesSub4ViewController alloc]
								   initWithNibName:@"ModulesSub4ViewController"
								   bundle:[NSBundle mainBundle]];
		self.sub4ViewController.title = @"Find Library";
	}
	
	
	if (indexPath.row == 0){
		[[self view] addSubview:self.sub1ViewController.view];
		//[self.navigationController pushViewController:self.sub1ViewController animated:YES];
	} 
	
	if (indexPath.row == 1){
		[[self view] addSubview:self.loginViewController.view];
		//[self.navigationController pushViewController:self.loginViewController animated:YES];
	}
	
	if (indexPath.row == 2){
		[[self view] addSubview:self.sub4ViewController.view];
			//[self.navigationController pushViewController:self.sub4ViewController animated:YES];
	} 

	/*if (indexPath.row == 3) {
			[self.navigationController pushViewController:self.sub4ViewController animated:YES];
	}*/
	
		
}


#pragma mark -
#pragma mark Memory management

- (void)didReceiveMemoryWarning {
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Relinquish ownership any cached data, images, etc that aren't in use.
}

- (void)viewDidUnload {
    // Relinquish ownership of anything that can be recreated in viewDidLoad or on demand.
    // For example: self.myOutlet = nil;
}


- (void)dealloc {
    [super dealloc];
}


@end

