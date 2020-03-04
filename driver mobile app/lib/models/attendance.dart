import 'package:flutter/material.dart';

class Attendance extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
     body:ListView(
       children: <Widget>[
             
                
             Column(
               mainAxisAlignment: MainAxisAlignment.center,
         children: <Widget>[
               Container(
                width: double.infinity,
                padding: EdgeInsets.all(30.0),
              
        
           child:RaisedButton(
              
                              onPressed: (){
                                //Navigator.of(context).pushNamed("/fourth");
                              },
                              padding: EdgeInsets.symmetric(vertical: 16.0, ),
                            color: Colors.pink,
                            elevation: 11,
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40.0))),
                          child: Text("Request Attendance", style: TextStyle(color: Colors.white70),),                    
                          ),),
                          SizedBox(height: 20.0),
                           Container(
                width: double.infinity,
                padding: EdgeInsets.all(30.0),
              
        
           child:RaisedButton(
                              onPressed: (){
                                //Navigator.of(context).pushNamed("/fourth");
                              },
                              
                              padding: EdgeInsets.symmetric(vertical: 16.0),
                            color: Colors.pink,
                            elevation: 11,
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40.0))),
                          child: Text("View Attendance", style: TextStyle(color: Colors.white70),),                    
                          ),
               ),
         ]
       
       ),
       ]
       ),
       
     );

    

  
    
  }
}