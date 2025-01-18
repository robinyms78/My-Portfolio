//
//  GooglePlaceAPIViewController.m
//  GooglePlaceAPI
//
//  Created by Robin Yap on 5/27/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import "GooglePlaceAPIViewController.h"
#import "JSON.h"

@implementation GooglePlaceAPIViewController

@synthesize activityIndicatorView, nearestlibrary, searchlatlong, buffer; 

- (IBAction)search {
    
	[activityIndicatorView startAnimating];
	
	//NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"https://maps.googleapis.com/maps/api/place/search/json?location=%@&radius=500&name=library&sensor=false&key=AIzaSyCpH7U3L4JHd1BUpMKjjjYtf8yf0NA9twA", searchlatlong]];
	//NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"https://maps.googleapis.com/maps/api/place/search/json?location=\"40.714728,-73.998672\"&radius=500&name=library&sensor=false&key=AIzaSyCpH7U3L4JHd1BUpMKjjjYtf8yf0NA9twA"]];
	NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"https://maps.googleapis.com/maps/api/place/search/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&sensor=false&key=AIzaSyCpH7U3L4JHd1BUpMKjjjYtf8yf0NA9twA"]];
	
	NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
	
	[request setHTTPMethod:@"GET"];
	
	conn = [[NSURLConnection alloc] initWithRequest:request delegate:self];
	
	if (conn) {
		self.buffer = [NSMutableData data];
	}
}

-(void) processResponse:(NSMutableData *) data {	
	
	NSMutableString *jsonString = [[NSMutableString alloc] initWithBytes:[data mutableBytes]
																  length: [data length]
																encoding: NSUTF8StringEncoding];
	NSDictionary *dictionary = [jsonString JSONValue];
	
	NSDictionary *dictionaryReturn = (NSDictionary*) [dictionary objectForKey:@"results"];
	//NSLog(@"Results count is %@", dictionaryReturn);	
	//NSArray *arrName = (NSArray*) [dictionaryReturn objectForKey:@"name"];
	
	//for(int n = 0; n <[arrName count] ; n++) {
	for (NSDictionary *location in dictionaryReturn) {		
		//NSDictionary *dictionaryArr = (NSDictionary*) [arrName objectAtIndex:n];
		//NSString *name = (NSString*) [dictionaryArr objectForKey:@"name"];
		NSString *name = (NSString*) [location objectForKey:@"name"];
		
		NSLog(@"Nearest Library:%@", name);
	}		
	
	[jsonString release];
	
	[activityIndicatorView stopAnimating];
	
}

- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response {
    [buffer setLength:0];
}

- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data {
    [buffer appendData:data];
}

- (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error {
	NSLog(@"Error during connection: %@", [error description]);
	[buffer release];
	[connection release];
}

- (void)connectionDidFinishLoading:(NSURLConnection *)connection {
    
    NSLog(@"Done with bytes: %d",[buffer length]);
	[self processResponse:buffer];
	[connection release];
	
	[activityIndicatorView stopAnimating];
}

-(void) dealloc {
	[super dealloc];
}

@end
