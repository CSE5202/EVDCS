import 'dart:ui';
import 'package:flutter/material.dart';
import './models/attendance.dart' as attendance;
import './models/notification.dart' as notification;
import './models/view.dart' as view;
import 'package:sampleproject2/utils/OvalRightBorderClipper.dart';
import 'package:flare_flutter/flare_actor.dart';
import 'package:wave/config.dart';
import 'package:wave/wave.dart';
//import 'package:assets/flare/bus.flr';
import './models/history.dart' as history;
//import './models/setting.dart' as setting;
import './models/profile.dart' as profile;
import 'dart:io';
//import 'package:sampleproject2/models/animation/animation1/animation1.dart';
//import 'package:sampleproject2/models/Homepage.dart';

//import 'package:sampleproject2/models/splashscreen.dart';

void main() {
  runApp(MaterialApp(
    home: new splashscreen(),
 routes: <String,WidgetBuilder>{
     "/second": (BuildContext context) => new authentication(),
     "/third": (BuildContext context) => new activation(),
     "/fourth":(BuildContext context) => new HomePage(),
     "/fifth":(BuildContext context) => new SettingPage(),
     "/sixth":(BuildContext context) => new history.History(),
     "/seventh":(BuildContext context) => new profile.Profile() ,
  }
 ));
}
class splashscreen extends StatefulWidget {
  @override
   splashscreenState createState() =>  splashscreenState();
}
const brightyellow = Color(0xFFFFD300);
const darkyellow = Color(0xFFFFB900);
class  splashscreenState extends State <splashscreen> {
    @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: brightyellow,
      body: Column(
        children: [
          Flexible(
            flex: 8,
            child: FlareActor(
              'assets/flare/bus.flr',
              alignment: Alignment.center,
              fit: BoxFit.contain,
              animation: 'driving',
            ),
          ),
          Flexible(
            flex: 2,
            child: RaisedButton(
              color: darkyellow,
              elevation: 4,
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(50)),
              child: Text(
                'Tap here to proceed',
                style: TextStyle(color: Colors.black54),
              ),
              onPressed: () {
                Navigator.of(context).pushNamed("/second");
              }//=>  Navigator.push(context, MaterialPageRoute(builder: (context)=>authentication()))
            ),
          ),
        ],
      ),
    );
  }
} 

class authentication extends StatelessWidget {
 
   Widget build(BuildContext context)  {
    return MaterialApp(
      home:Scaffold(
        //backgroundColor: Colors.purple.withOpacity(0.5),
        body: Stack(
          children: <Widget>[
            Container(
              height: 650,
              child: RotatedBox(quarterTurns: 2,
              child: WaveWidget(
                config: CustomConfig( 
                  gradients: [
                    [Colors.deepPurple,Colors.deepPurple.shade200],
                    [Colors.indigo.shade200, Colors.purple.shade200],
                    ],
                  durations: [19440,10800], 
                  heightPercentages:[ 0,20,0,25],
                  blur: MaskFilter.blur(BlurStyle.solid, 10),
                  gradientBegin: Alignment.bottomLeft,
                  gradientEnd: Alignment.topRight
               
              ),
              waveAmplitude: 0,
              size: Size(
                double.infinity,
                double.infinity,
              ),
              ),
            ),
            ),
            ListView(children: <Widget>[
              Container(
                height:400,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children:<Widget>[
                    Text("Please insert your phone number to get activation key",textAlign: TextAlign.center,style: TextStyle(color: Colors.white70,fontWeight:FontWeight.bold,fontSize:18.0) ),
                    Card(
                      margin: EdgeInsets.only(left: 30, right:30, top: 50),
                      elevation: 11,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40))),
                      child: TextField(
                        decoration: InputDecoration(
                          prefixIcon: Icon(Icons.phone, color: Colors.black26,),
                          hintText: "phone no",
                          hintStyle: TextStyle( 
                            color: Colors.black26,
                          ),
                          filled: true,
                          fillColor: Colors.white,
                          border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(40.0)),
                          borderSide: BorderSide.none),
                          contentPadding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 16.0)

                        ),
                      )
                    ),
                    Container(
                      width: double.infinity,
                      padding: EdgeInsets.all(30.0),
                      child: RaisedButton(
                        onPressed: (){
                          Navigator.of(context).pushNamed("/third");
                        },
                        padding: EdgeInsets.symmetric(vertical: 16.0),
                      color: Colors.pink,
                      elevation: 11,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40.0))),
                    child: Text("submit", style: TextStyle(color: Colors.white70),),                    
                    ),
                    ),

                  ],
                ),

              )
             
          ],
        )
       ]
      ),
  ));
  }

  
}
class activation extends StatelessWidget {
 
   Widget build(BuildContext context)  {
    return MaterialApp(
      home:Scaffold(
        //backgroundColor: Colors.purple.withOpacity(0.5),
        body: Stack(
          children: <Widget>[
            Container(
              height: 650,
              child: RotatedBox(quarterTurns: 2,
              child: WaveWidget(
                config: CustomConfig( 
                  gradients: [
                    [Colors.deepPurple,Colors.deepPurple.shade200],
                    [Colors.indigo.shade200, Colors.purple.shade200],
                    ],
                  durations: [19440,10800], 
                  heightPercentages:[ 0,20,0,25],
                  blur: MaskFilter.blur(BlurStyle.solid, 10),
                  gradientBegin: Alignment.bottomLeft,
                  gradientEnd: Alignment.topRight
               
              ),
              waveAmplitude: 0,
              size: Size(
                double.infinity,
                double.infinity,
              ),
              ),
            ),
            ),
            ListView(children: <Widget>[
              Container(
                height:400,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children:<Widget>[
                    Text("Please insert your activation key",textAlign: TextAlign.center,style: TextStyle(color: Colors.white70,fontWeight:FontWeight.bold,fontSize:18.0) ),
                    Card(
                      margin: EdgeInsets.only(left: 30, right:30, top: 20),
                      elevation: 11,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40))),
                      child: TextField(
                        decoration: InputDecoration(
                          prefixIcon: Icon(Icons.vpn_key, color: Colors.black26,),
                          hintText: "activation key",
                          hintStyle: TextStyle( 
                            color: Colors.black26,
                          ),
                          filled: true,
                          fillColor: Colors.white,
                          border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(40.0)),
                          borderSide: BorderSide.none),
                          contentPadding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 16.0)

                        ),
                      )
                    ),
                    Container(
                      width: double.infinity,
                      padding: EdgeInsets.all(30.0),
                      child: RaisedButton(
                        onPressed: (){
                          Navigator.of(context).pushNamed("/fourth");
                        },
                        padding: EdgeInsets.symmetric(vertical: 16.0),
                      color: Colors.pink,
                      elevation: 11,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(40.0))),
                    child: Text("Go", style: TextStyle(color: Colors.white70),),                    
                    ),
                    ),

                  ],
                ),

              )
             
          ],
        )
       ]
      ),
  ));
  }

  
}

 class HomePage extends StatefulWidget {
    @override
    HomePage_State createState() => HomePage_State();
  }
  
  class HomePage_State extends State<HomePage> with SingleTickerProviderStateMixin{
    final Color primary = Color(0xff291747);
    Widget StylishDrawer(){
      return ClipPath(
        clipper:OvalRightBorderClipper(),
        child: Container(
          width: 300,
          child: Stack(
            children: <Widget>[
              BackdropFilter(filter: ImageFilter.blur(sigmaX:5.0, sigmaY: 5.0),
              child: Container(
                decoration: BoxDecoration(
                  color: primary,
                )

              ),
              ),
              Container(
                child: ListView(
                  children: <Widget>[
                    Column(
                      children: <Widget>[
                        Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: SizedBox(
                            width: 100,
                            height: 100,
                            child: CircleAvatar(backgroundImage: AssetImage('assets/B612-2019-11-23-11-30-00.jpg'),
                            )
                          ),
                        ),
                        Text("xyz",style: TextStyle(color: Colors.white),
                        ),
                      ],
                    ),
                    SizedBox(height: 60),
                    Divider(height: 0.5, color:Colors.black54,),
                    ListTile(
                      leading: Icon(Icons.home,color:Colors.white,), 
                    title: Text("Home",style:TextStyle(color: Colors.white),
                   ),
                   onTap: (){
                     Navigator.of(context).pushNamed("/fourth");

                   },
                    ),
                    
                    ListTile(
                      leading: Icon(Icons.person_pin,color:Colors.white,), 
                    title: Text("Profile",style:TextStyle(color: Colors.white),
                    ),
                    onTap: (){
                     Navigator.of(context).pushNamed("/seventh");
                   },
                    ),
                      
                    ListTile(
                      leading: Icon(Icons.settings,color:Colors.white,), 
                    title: Text("Setting",style:TextStyle(color: Colors.white),
                    ),
                    onTap: (){
                     Navigator.of(context).pushNamed("/fifth");
                   },
                    ),
                     ListTile(
                      leading: Icon(Icons.history,color:Colors.white,), 
                    title: Text("History",style:TextStyle(color: Colors.white),
                    ),
                    onTap: (){
                     Navigator.of(context).pushNamed("/sixth");
                   },
                    ),
                    SizedBox(height: 50),
                    SizedBox(width: 50),
                    ListTile(
                      leading: Icon(Icons.settings_power,color:Colors.white,), 
                    title: Text("Quit",style:TextStyle(color: Colors.white),
                    ),
                    onTap: (){exit(0);}
                   
                    ),

                   
                  ]
                )

              ),
            ],
          )
        )
      );

    }
    
    @override
    Widget build(BuildContext context) {
      return MaterialApp(
        home: DefaultTabController(
          length: 3,
          child: Scaffold(
          drawer: StylishDrawer(),
          appBar: AppBar(
            title: Text('Driver App',style: TextStyle(color: Colors.white,fontSize: 18.0)),
            backgroundColor: Colors.purple.withOpacity(0.5),
            bottom: new TabBar(
              //controller: controller,
              tabs: <Tab>[
                new Tab(icon: Icon(Icons.notifications,)),
                new Tab(icon: Icon(Icons.remove_red_eye)),
                new Tab(icon: Icon(Icons.calendar_view_day)),
              ]
            )
          ),
          body: new TabBarView(
            //controller: controller,
            children: <Widget>[
              new notification.Notification(),
              new view.View(),
              new attendance.Attendance(),
              
              
            ],

          )
        )
        
      )
      );
    }
  } 
  class SettingPage extends StatelessWidget {
 
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade200,
      appBar: AppBar(
        elevation: 0,
        brightness: Brightness.light,
        backgroundColor: Colors.purple.withOpacity(0.5),
      title: Text('Setting', style: TextStyle(color: Colors.white70,fontSize: 20.0,fontWeight: FontWeight.bold,)
      ),
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text("Notification Setting",
            style: TextStyle(color: Colors.indigo,fontSize: 20.0,fontWeight: FontWeight.bold,),
            ),
            SwitchListTile(
              dense: true,
              activeColor: Colors.purple,
              contentPadding: const EdgeInsets.all(0),
              value: true,
              title: Text('Recieved notification'),
              onChanged: (val){},
            )
          ],

      ),
      ),
      
      
    );
  }
}

