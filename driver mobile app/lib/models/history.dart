import 'package:flutter/material.dart';
class History extends StatefulWidget {
  @override
  _HistoryState createState() => _HistoryState();
}

class _HistoryState extends State<History> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade200,
      appBar: AppBar(
        elevation: 0,
        brightness: Brightness.light,
        backgroundColor: Colors.purple.withOpacity(0.5),
        title: Text("History", style:TextStyle(color: Colors.white70,fontSize: 20.0,fontWeight: FontWeight.bold,)
      )
      ),
      body: ListView(
      
        children: <Widget>[
          Card(
            
            //mainAxisAlignment: MainAxisAlignment.start,
            //children: <Widget>[
            child: Text("Route History",
            style: TextStyle(color: Colors.black,fontSize: 20.0,fontWeight: FontWeight.bold,),
            ),),
            SizedBox(width: 20),
             Container(
                      width: double.infinity,
                      padding: EdgeInsets.all(30.0),
            child:RaisedButton(onPressed: null,color: Colors.pink,padding: EdgeInsets.symmetric(vertical: 16.0),
            elevation: 11,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40.0))),
            child: Text("view",style: TextStyle(color: Colors.white70)))
            //],
           
          ),
          SizedBox(height:30),
           Card(
            
            //mainAxisAlignment: MainAxisAlignment.start,
            //children: <Widget>[
            child: Text("Penality History",
            style: TextStyle(color: Colors.black,fontSize: 20.0,fontWeight: FontWeight.bold,),
            ),),
            SizedBox(width: 20),
             Container(
                      width: double.infinity,
                      padding: EdgeInsets.all(30.0),
            child:RaisedButton(onPressed: null,color: Colors.pink ,padding: EdgeInsets.symmetric(vertical: 16.0),
            elevation: 11,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40.0))),
            child: Text("view",style: TextStyle(color: Colors.white70)
            )
            )
            //],
           
          ),]

      )

      
    );
  }
}