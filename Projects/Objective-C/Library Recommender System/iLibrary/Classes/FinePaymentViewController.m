//
//  FinePaymentViewController.m
//  FinePayment
//
//  Created by student on 5/31/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "FinePaymentViewController.h"
#import "IFChargeRequest.h"


@implementation FinePaymentViewController
@synthesize fineAmount,booksModel;

- (IBAction)payFine:(id)sender
{
	[[[UIAlertView alloc] initWithTitle:@"Alert" message:@"starting payment" delegate:nil cancelButtonTitle:@"Ok" otherButtonTitles:nil] show];
	
	/*
    IFChargeRequest* chargeRequest = [[[IFChargeRequest alloc] init] autorelease];
	[chargeRequest setReturnURL:@"com-innerfence-ChargeDemo://chargeResponse"
				withExtraParams:[NSDictionary dictionaryWithObjectsAndKeys:
								 @"123", @"record_id",
								 nil]];
	
    chargeRequest.address        = @"Clementi Street 1";
    chargeRequest.amount         = @"50.00";
    chargeRequest.currency       = @"SGD";
    chargeRequest.city           = @"Singapore";
    chargeRequest.company        = @"Company Inc";
    chargeRequest.country        = @"SG";
    chargeRequest.description    = @"Test transaction";
    chargeRequest.email          = @"saima@example.com";
    chargeRequest.firstName      = @"Saima";
    chargeRequest.invoiceNumber  = @"321";
    chargeRequest.lastName       = @"Ashraf";
    chargeRequest.phone          = @"555-1212";
    chargeRequest.state          = @"Singapore";
    chargeRequest.zip            = @"98021";
	
    [chargeRequest submit];
	 */
}

- (void)dealloc {
    [super dealloc];
}

@end
