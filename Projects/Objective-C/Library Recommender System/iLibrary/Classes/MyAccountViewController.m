//
//  RootViewController.m
//  MyAccount
//
//  Created by Mok Hei Chee on 5/31/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "MyAccountViewController.h"
#import "MyAccountModel.h";
#import "MyAccountSub1ViewController.h";
#import "MyAccountSub2ViewController.h";
#import "MyAccountSub3ViewController.h";
#import "BooksModel.h"
#import "ReaderSampleViewController.h"
#import "FinePaymentViewController.h"

@implementation MyAccountViewController

@synthesize myAccountModel, sub1ViewController, sub2ViewController, sub3ViewController,userId,booksModel,eventArray,eventStore; 

#pragma mark -
#pragma mark View lifecycle


- (void)viewDidLoad {
    [super viewDidLoad];

    // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
    // self.navigationItem.rightBarButtonItem = self.editButtonItem;
	NSLog(@"The user Id is %@",self.userId);
	NSLog(@"AccountViewController viewbooksModelDidLoad%i",booksModel.count);
	self.title = @"My Account";
	myAccountModel = [[MyAccountModel alloc] init];
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
    return myAccountModel.arrayData.count;
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
	cell.textLabel.text = [myAccountModel.arrayData objectAtIndex:row];
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
		self.sub1ViewController = [[MyAccountSub1ViewController alloc]
								   initWithNibName:@"MyAccountSub1ViewController"
								   bundle:[NSBundle mainBundle]];
		self.sub1ViewController.title = @"Account Details";
	}
	
	if (self.sub2ViewController == nil){
								   
	ReaderSampleViewController *readerViewController= [[ReaderSampleViewController alloc] initWithNibName:@"ReaderSampleViewController" bundle:[NSBundle mainBundle]];
	[readerViewController setBooksModel:self.booksModel];		
	[[self view] addSubview:readerViewController.view];

	}
	
	if (self.sub3ViewController == nil){
		self.sub3ViewController = [[MyAccountSub3ViewController alloc]
								   initWithNibName:@"MyAccountSub3ViewController"
								   bundle:[NSBundle mainBundle]];
		self.sub3ViewController.title = @"Set Alerts";
		
		for (BooksModel *item in self.booksModel) {
			NSLog(@"BooksModel dueDate %@",item.dueDate);
			
			
			EKEventStore *eventStore1 = [[EKEventStore alloc] init];
			
			double alarmAmountInSeconds = 60.0 * 60.0 * 24.0;
			EKAlarm *alarm = [EKAlarm alarmWithRelativeOffset:(-1.0 * alarmAmountInSeconds)];
			
			EKEvent *myEvent = [EKEvent eventWithEventStore:eventStore1];
			myEvent.calendar = eventStore1.defaultCalendarForNewEvents;
			myEvent.title = @"My Book Due Date"; 
			myEvent.startDate = item.dueDate; 
			myEvent.endDate = item.dueDate; 
			myEvent.allDay = TRUE; 
			//myEvent.recurrenceRule =recurrance; 
			myEvent.alarms = [NSArray arrayWithObject:alarm]; 
			myEvent.notes = @"Remember to Return the Book or Renew the Book!";
			
			NSError *err = nil;
			BOOL result = [eventStore1 saveEvent:myEvent span: EKSpanFutureEvents error:&err];
			
			if (!result) {
				NSLog(@"Error Saving Event for %@",item.dueDate);
			}else{
				NSLog(@"Event Saved");
			}
			
		[eventStore1 release];
			
			
		} 
		
		
		
		
	}
	
	if(indexPath.row == 0){
		[self.navigationController pushViewController:self.sub1ViewController animated:YES];
	} 
	
	if(indexPath.row == 1){
		[self.navigationController pushViewController:self.sub2ViewController animated:YES];
	}
	
	if(indexPath.row == 2){
		[self.navigationController pushViewController:self.sub3ViewController animated:YES];
	}
			
	if(indexPath.row == 3){
		FinePaymentViewController *fineViewController=  [[FinePaymentViewController alloc] initWithNibName:@"FinePaymentViewController" bundle:[NSBundle mainBundle]];
		[fineViewController setBooksModel:self.booksModel];	
		
		[[fineViewController fineAmount] setText:@"$ 0.00"];
		[[self view] addSubview:fineViewController.view];
	}
}


#pragma mak -
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

