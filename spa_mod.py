import ctypes

spa = ctypes.CDLL('./spa.so')

class SpaData(ctypes.Structure):
     _fields_ = [
("year", ctypes.c_int),            					
("month", ctypes.c_int),           
("day", ctypes.c_int),             
("hour", ctypes.c_int),            
("minute", ctypes.c_int),          
("second", ctypes.c_double),       
("delta_ut1", ctypes.c_double),              
("delta_t", ctypes.c_double),     
("timezone", ctypes.c_double),            
("longitude", ctypes.c_double),                        
("latitude", ctypes.c_double),                         
("elevation", ctypes.c_double),                         
("pressure", ctypes.c_double),                         
("temperature", ctypes.c_double),
("slope", ctypes.c_double),                          
("azm_rotation", ctypes.c_double),             
("atmos_refract", ctypes.c_double),                    
("function", ctypes.c_int),
("jd", ctypes.c_double),         
("jc", ctypes.c_double),         
("jde", ctypes.c_double),        
("jce", ctypes.c_double),        
("jme", ctypes.c_double),        
("l", ctypes.c_double),          
("b", ctypes.c_double),          
("r", ctypes.c_double),          
("theta", ctypes.c_double),      
("beta", ctypes.c_double),       
("x0", ctypes.c_double),         
("x1", ctypes.c_double),         
("x2", ctypes.c_double),         
("x3", ctypes.c_double),         
("x4", ctypes.c_double),         
("del_psi", ctypes.c_double),    
("del_epsilon", ctypes.c_double),
("epsilon0", ctypes.c_double),   
("epsilon", ctypes.c_double),    
("del_tau", ctypes.c_double),    
("lamda", ctypes.c_double),      
("nu0", ctypes.c_double),        
("nu", ctypes.c_double),         
("alpha", ctypes.c_double),      
("delta", ctypes.c_double),      
("h", ctypes.c_double),          
("xi", ctypes.c_double),         
("del_alpha", ctypes.c_double),  
("delta_prime", ctypes.c_double),
("alpha_prime", ctypes.c_double),
("h_prime", ctypes.c_double),    
("e0", ctypes.c_double),         
("del_e", ctypes.c_double),      
("e", ctypes.c_double),          
("eot", ctypes.c_double),        
("srha", ctypes.c_double),       
("ssha", ctypes.c_double),       
("sta", ctypes.c_double),      
("zenith", ctypes.c_double),       
("azimuth_astro", ctypes.c_double),
("azimuth", ctypes.c_double),      
("incidence", ctypes.c_double),    
("suntransit", ctypes.c_double),   
("sunrise", ctypes.c_double),      
("sunset", ctypes.c_double)
]                        

data = SpaData(
2003,
10,
17,
12,
33,
10.0,
0.0,
0.0,
0.0,
-105.1786,
39.78,
0,
820.0,
15.0,
0,
0,
0.5567,
3,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.0)

result = spa.spa_calculate(ctypes.byref(data))

#returns a dict with status, zenith and azimuth
def calculate_position(year, month, day, hour, minute, second, latitude, longitude):
	data.year 		=  year 	
	data.month 		=  month 	
	data.day 		=  day 	
	data.hour 		=  hour 	
	data.minute 	=  minute 
	data.second 	=  second 
	data.latitude 	=  latitude 
	data.longitude 	=  longitude
	
	result = spa.spa_calculate(ctypes.byref(data))
	
	return {'status': result, 'zenith': data.zenith, 'azimuth': data.azimuth}

print('Zenith: ' + str(data.zenith) + ', Azimuth: ' + str(data.azimuth))


