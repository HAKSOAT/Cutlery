This test URL shortner is currently hosted at [cutlery](https://cutlery.herokuapp.com) and has the following end points:

 - generate-random-url
	 - Endpoint requires the following parameters: link.
	 - Example:
		 - {'link': 'http://linuxhint.com/author/kenny'}
	 - Endpoint returns a result similar to the following:
		 - { "link": "http://linuxhint.com", "alias": "BDFHTTY", "generated_link": "cutlery.herokuapp.com/BDFHTTY"}
 - generate-custom-url
	 - Endpoint requires the following parameters: link, alias.
	 - Example:
		 - {'link': 'http://linuxhint.com/author/kenny', 'alias': 'haks'}
	 - Endpoint returns a result similar to the following:
		 - { "link": "http://linuxhint.com", "alias": "haks", "generated_link": "cutlery.herokuapp.com/haks"}

On visiting the generated link, [cutlery](https://cutlery.herokuapp.com) redirects to the original link.

