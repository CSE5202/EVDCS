import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';


class Profile extends StatefulWidget {
  @override
  _ProfileState createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  String company_name = "Sheger Bus";
  String position = "Driver";
  String duration = "20 years";

  String city = "AddisAbaba";
  String subcity="Arada";
  String kebele="06";
  String phoneno = "09456789";
  String vehicle_type ="bus";
  String vehiecle_no ="1234";
  String licence_no="2345";

  String driver_name="xyz";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade200,
      appBar: AppBar(
        elevation: 0,
        brightness: Brightness.light,
        backgroundColor: Colors.purple.withOpacity(0.5),
        title: Text("Profile", style:TextStyle(color: Colors.white70,fontSize: 20.0,fontWeight: FontWeight.bold,)
      )
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            _buildHeader(driver_name),
            _buildTitle("Experience"),
            _buildExperienceRow(company_name,position,duration),
            SizedBox(height: 20.0,),
            _buildTitle("Adress"),
            SizedBox(height: 5.0,),
            _buildAdressRow(city,subcity,kebele),
            SizedBox(height: 20.0,),
            _buildTitle("Contact"),
             SizedBox(height: 5.0,),
             Row(children: <Widget>[
               SizedBox(height: 30.0,),
               Icon(Icons.phone,color: Colors.black54,),
               SizedBox(height: 10.0,),
               Text(phoneno, style: TextStyle(color: Colors.black54,fontSize: 16.0))
             ],),
            SizedBox(height: 10.0,),
            _buildTitle("Vehicle"),
            SizedBox(height: 10.0,),
            _buildVehicleRow(vehicle_type,vehiecle_no,licence_no),


          ]
        )
      ),
    );
    
  }
  _buildExperienceRow(String Company_Name, String Position, String Duration){
      return ListTile(leading:Padding(
       padding: const EdgeInsets.only(top: 8.0, left: 20.0),
        child: Icon(FontAwesomeIcons.solidCircle,size:12.0,color: Colors.black54,),
      ),
       title: Text("$Company_Name",style: TextStyle(color: Colors.black,fontWeight: FontWeight.bold,)),
       subtitle: Text("$Position($Duration)"),
      );
    }
     _buildAdressRow(String city,String subcity,String kebele){
       return ListTile(leading:Padding(
        padding: const EdgeInsets.only(top: 8.0, left: 20.0),
        child: Icon(FontAwesomeIcons.solidCircle,size:12.0,color: Colors.black54,),
      ),
       title: Text("$city",style: TextStyle(color: Colors.black,fontWeight: FontWeight.bold,)),
       subtitle: Text("$subcity($kebele)"),
      );


     }
      _buildVehicleRow(String vehicle_type,String vehiecle_no,String licence_no){
          return ListTile(leading:Padding(
       padding: const EdgeInsets.only(top: 8.0, left: 20.0),
        child: Icon(FontAwesomeIcons.solidCircle,size:12.0,color: Colors.black54,),
      ),
       title: Text("$vehicle_type",style: TextStyle(color: Colors.black,fontWeight: FontWeight.bold,)),
       subtitle: Text("$vehiecle_no($licence_no)"),
      );

      }
      _buildTitle(String title){
        return Padding(
          padding: const EdgeInsets.only(left:16.0),
         child: Column(
           crossAxisAlignment: CrossAxisAlignment.start,
           children: <Widget>[
             Text(title.toUpperCase(),style: TextStyle(fontSize: 18.0,fontWeight: FontWeight.bold,)),
             Divider(color: Colors.black54,),
           ],

         )
        );

      }
      Row _buildHeader(String driver_name){
        return Row(children: <Widget>[
          SizedBox(width: 20.0,),
          Container(
            width: 80.0,
            height: 80.0,
            child: CircleAvatar(
              radius:40,
              backgroundColor: Colors.grey,
              child: CircleAvatar(
              radius:40,
              //backgroundImage: ,
              ),)
              ),
             SizedBox(width: 20.0),
             Column(
               crossAxisAlignment: CrossAxisAlignment.start,
               children: <Widget>[
                 Text("$driver_name",style: TextStyle(fontSize: 18.0,fontWeight: FontWeight.bold,)),
                 SizedBox(height: 40.0),
                 
               ],

             )

         

        ],);
      }
}
