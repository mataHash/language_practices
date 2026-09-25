unsigned int gcd( unsigned int u, unsigned int v){

	while (u != 0) {
		if (u < v) {
			u = u ^ v;
			v = u ^ v;
			u = u ^ v;
		}
		else {
			u -=v;
		}
	}
	return v;
}
