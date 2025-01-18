//
//  GooglePlaceSearchViewController.m
//  GooglePlaceSearch
//
//  Created by Robin Yap on 6/5/11.
//  Copyright 2011 NUS. All rights reserved.
//

#import "GooglePlaceSearchViewController.h"
#import "JSON.h"

@implementation GooglePlaceSearchViewController

@synthesize activityIndicatorView, latitude, longitude, buffer; 

- (IBAction) lookup {
	
	NSNumber *latitude = latitude.text;
	
	NSNumber *longitude = longitude.text;
	
	NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"https://maps.googleapis.com/maps/api/place/search/json?location=%@,%@&radius=500&name=library&sensor=false&key=AIzaSyCpH7U3L4JHd1BUpMKjjjYtf8yf0NA9twA", latitude.text, longitude.text]];
	
	NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
	
	[request setHTTPMethod:@"GET"];
	
	conn = [[NSURLConnection alloc] initWithRequest:request delegate:self];
	
	if (conn) {
		self.buffer = [NSMutableData data];
	}
	[activityIndicatorView startAnimating];		
}

-(void)connectionDidFinishLoading:(NSURLConnection *)connection {	
	
	[connection release];
	
	NSMutableString *jsonString = [[NSMutableString alloc] initWithBytes:[buffer mutableBytes]
																  length: [buffer length]
																encoding: NSUTF8StringEncoding];
	
	[buffer release];
	
	NSDictionary *dictionary = [jsonString JSONValue];
	
	NSDictionary *dictionaryReturn = (NSDictionary*) [dictionary objectForKey:@"return"];
	
	NSArray *arrName = (NSArray*) [dictionaryReturn objectForKey:@"name"];
	
	for(int n = 0; n <[arrName count] ; n++) {
		
		NSDictionary *dictionaryArr = (NSDictionary*) [arrName objectAtIndex:n];
		
		NSString *name = (NSString*) [dictionaryArr objectForKey:@"name"];
		
		nearestlibrary.text = name;
		
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

-(void) dealloc {
	[super dealloc];
}

@end
