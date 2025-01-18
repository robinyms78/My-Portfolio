//
//  FinePaymentViewController.h
//  FinePayment
//
//  Created by student on 5/31/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface FinePaymentViewController : UIViewController {
	UILabel *fineAmount;
	NSMutableArray *booksModel;
}

@property(nonatomic,retain)NSMutableArray *booksModel;
@property (nonatomic,retain) IBOutlet UILabel *fineAmount;
- (IBAction)payFine:(id)sender;

@end

