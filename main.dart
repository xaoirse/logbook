import 'dart:convert';
// import 'dart:html';
import 'package:encrypt/encrypt.dart' as en;

import 'package:flutter_localizations/flutter_localizations.dart';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:http/http.dart' as http;



void main() => runApp(MyApp());


var username = {'username':'','name':'','token':''};
var response = {"status": "ok", "interships": [{"name": "بزرگسالان 1", "term": "981", "students": [{"name": "امیر جامی", "num": "96140005", "items": [{"name": "خون گیری", "count": 0, "min": 4}, {"name": "گزارش نویسی", "count": 0, "min": 5}, {"name": "شرح حال", "count": 0, "min": 6}, {"name": "آماده کردن صحیح دارو", "count": 0, "min": 5}]}, {"name": "علی بیدخوری", "num": "96140002", "items": [{"name": "خون گیری", "count": 0, "min": 4}, {"name": "گزارش نویسی", "count": 0, "min": 5}, {"name": "شرح حال", "count": 0, "min": 6}, {"name": "آماده کردن صحیح دارو", "count": 0, "min": 5}]}, {"name": "امیر رضا خوشدل", "num": "96140004", "items": [{"name": "خون گیری", "count": 0, "min": 4}, {"name": "گزارش نویسی", "count": 0, "min": 5}, {"name": "شرح حال", "count": 0, "min": 6}, {"name": "آماده کردن صحیح دارو", "count": 0, "min": 5}]}, {"name": "پارسا", "num": "96140003", "items": [{"name": "خون گیری", "count": 0, "min": 4}, {"name": "گزارش نویسی", "count": 0, "min": 5}, {"name": "شرح حال", "count": 0, "min": 6}, {"name": "آماده کردن صحیح دارو", "count": 0, "min": 5}]}]}, {"name": "اطفال", "term": "981", "students": [{"name": "امیر جامی", "num": "96140005", "items": [{"name": "مراقبت از کودک", "count": 0, "min": 4}, {"name": "مراقبت از نوزاد", "count": 0, "min": 4}]}, {"name": "علی بیدخوری", "num": "96140002", "items": [{"name": "مراقبت از کودک", "count": 0, "min": 4}, {"name": "مراقبت از نوزاد", "count": 0, "min": 4}]}, {"name": "امیر رضا خوشدل", "num": "96140004", "items": [{"name": "مراقبت از کودک", "count": 0, "min": 4}, {"name": "مراقبت از نوزاد", "count": 0, "min": 4}]}, {"name": "پارسا", "num": "96140003", "items": [{"name": "مراقبت از کودک", "count": 0, "min": 4}, {"name": "مراقبت از نوزاد", "count": 0, "min": 4}]}]}]};
var response2 ;

var master = {'username':'','name':'','token':''};
var terms;
var selectedTerm;
var groups;
var studentInfo = {'name':'','num':''};
var items;
var items4send = {};
int tag;


class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    
    return MaterialApp(
      localizationsDelegates: [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ],
      supportedLocales: [
        Locale("fa", "IR"), 
      ],
      locale: Locale("fa", "IR"),
      title: 'nurselog',
      theme: ThemeData(
        fontFamily: 'Vazir',
      ),
      home: LoginPage()
    );
  }
}


class LoginPage extends StatelessWidget {
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  Future<http.Response> loggingIn(context) async {
    Fernet f = new Fernet() ;
    return await http.post(
      "http://mylogbook.ir/app",
      body:{
        'username':usernameController.text,
        'password':passwordController.text,
      }
    );
  }



  // Login button click
  Future<void> loggingIn_(context) async {

    // var resp =  await fetchPost();
    // if (resp.statusCode==200){
    //   var jsonResp = jsonDecode(resp.body);
    //   String status = jsonResp['status'];
    //   if(status=='error'){
    //     usernameController.text='not match';
    //   }else{
    //     String token = jsonResp['token'];
    //     String name = jsonResp['name'];
    //     usernameController.text=name;
    //     passwordController.text=token;

        

    //   }
    // }else{
    //   usernameController.text=resp.statusCode as String;
    // }
    

  }
  bool isFirst = true;
  @override
  Widget build(BuildContext context) {

    return Scaffold(
      backgroundColor: Colors.lightBlue,
      body: SingleChildScrollView(
        child: Container(
          child: Container(
          margin: EdgeInsets.only(top: 70, left: 50,right:50,bottom: 50),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(10),
            color: Colors.white,
            boxShadow: [
              BoxShadow(
                color: Colors.grey[800],
                blurRadius: 1,
                spreadRadius: 0,
                offset: Offset(
                  0.1, 
                  0.1, 
                ),
              )
            ]
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              SizedBox(
                height: 10,
              ),
              Image(image: AssetImage(
                'assets/mainlogob.png'),
                height: 130,
                width: 130,
              ),
              Container(
                width: 200,
                decoration: BoxDecoration(
                  color: Colors.lightBlue,
                  borderRadius: BorderRadius.circular(5)
                ),
                // color: Colors.lightBlue,
                child: Text('دانشکده پرستاری',
                textAlign: TextAlign.center,
                style: 
                  TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Colors.white
                  ),
                  
                ),
              ),
              SizedBox(
                height: 5,
              ),
              Container(
                padding: EdgeInsets.only(right: 45,left: 45),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Expanded(
                      child: Column(
                        children: <Widget>[
                          Container(
                            // width: 200,
                            child: TextField(
                              controller: usernameController,
                              textAlign: TextAlign.end,
                              style: TextStyle(
                                color: Colors.black,
                                height: 1
                              ),
                              decoration: InputDecoration(
                                labelStyle: TextStyle(
                                  textBaseline: TextBaseline.alphabetic,
                                  // fontWeight: FontWeight.bold,
                                  color: Colors.blue[700]
                                ),
                                labelText: 'نام کاربری',
                                focusColor: Colors.indigo[900],
                                
                              ),
                            ),
                          ),
                          SizedBox(height: 10),
                          Container(
                            // width: 200,
                            child: TextField(
                              textAlign: TextAlign.end,
                              controller: passwordController,
                              obscureText: true,
                              style: TextStyle(
                                color: Colors.black,
                                height: 1
                              ),
                              decoration: InputDecoration(
                                labelStyle: TextStyle(
                                  color: Colors.blue[700],
                                  // fontWeight: FontWeight.bold,
                                ),
                                labelText: 'کلمه عبور',
                                focusColor: Colors.black,
                                
                              ),
                            ),
                          )
                        ],
                      ),
                    )
                  ],
                ),
              ),
              Container(
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Container(
                      margin: EdgeInsets.only(top: 20),
                      child: Text('Captcha test'),
                    ),  
                  ],
                ),
              ),
              Container(
                margin: EdgeInsets.all(20),
                child: Builder(
                  builder: (context){
                    return RaisedButton(
                      textColor: Colors.white,
                      color: Colors.lightBlue,
                      child: Container(
                        
                        child: Text('ورود',)
                      ),
                      onPressed: (){
                        // TODO insert .error
                        loggingIn(context).then((data){
                          if(jsonDecode(data.body)['status'] == 'ok'){
                            master['name'] = jsonDecode(data.body)['name'];
                            master['token'] = jsonDecode(data.body)['token'];
                            master['username'] = usernameController.text;
                            Navigator.push(context,MaterialPageRoute(builder: (context)=>HomePage(),));
                          }
                          else
                          Scaffold.of(context).showSnackBar(SnackBar(
                            content: Text(" مشکلی پیش آمده دوباره امتحان کنید."),
                          ));
                        });
                      },
                    );
                  },
                )
              ),
              Container(
                margin: EdgeInsets.only(top:5, bottom: 10),
                child: Text('رمز عبور را فراموش کردید؟'),
              )
            ]
          )
        )
        )
      )
    );
  }
}



class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  @override
  Widget build(BuildContext context) {
    // return Scaffold(
    //   appBar: AppBar(
    //     backgroundColor: Colors.lightBlue,
    //     title: Text('استاد',textAlign: TextAlign.center,),
    //   ),
    //   body: TermList(),
    // );
    return TermList();
  }
}

class TermList extends StatefulWidget {
  @override
  _TermListState createState() => _TermListState();
}

class _TermListState extends State<TermList> {

  termsList(){
    return ListView.builder(
      scrollDirection: Axis.horizontal,
      // physics: NeverScrollableScrollPhysics(),
      shrinkWrap: true,
      itemCount: terms['terms'].length,
      itemBuilder: (context, position){
        if (terms['terms'][position] == selectedTerm){
          return FlatButton(
            onPressed: (){
              setState(() {
                selectedTerm = terms['terms'][position];
              });
            },          
            child: Container(
              decoration: BoxDecoration(
                border: Border.all(width: 3,color: Colors.lightBlue),
                color: Colors.white,
                borderRadius: BorderRadius.circular(5)
                // shape: BoxShape.rectangle,
                // border: Border.all(width: 2)
              ),
              // height: 80,
              width: 100,
              margin: EdgeInsets.only(top:7,bottom: 7),
              alignment: AlignmentDirectional.center,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text('ترم ',style: TextStyle(color: Colors.lightBlue[600])),
                  Text('${terms["terms"][position]}',
                  style: TextStyle(
                    fontSize: 30,
                    color: Colors.lightBlue[600],
                  ),
                  ),
                ],
              ),
            )
          );
        }else{
          return FlatButton(
            onPressed: (){
              setState(() {
                selectedTerm = terms['terms'][position];
              });
            }, 
            child: Container(
              decoration: BoxDecoration(
                border: Border.all(width: 3,color: Colors.lightBlue[100]),
                color: Colors.white,
                borderRadius: BorderRadius.circular(5)
              ),
              width: 100,
              margin: EdgeInsets.only(top:7,bottom: 7),
              alignment: AlignmentDirectional.center,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text('ترم ',style: TextStyle(color: Colors.lightBlue[600])),
                  Text('${terms["terms"][position]}',
                  style: TextStyle(
                    fontSize: 30,
                    color: Colors.lightBlue[600],
                  ),
                  ),
                ],
              ),
            )
          );
        }
      },
    );
  }

  Route itemRoute() {
    return PageRouteBuilder(
      pageBuilder: (context, animation, secondaryAnimation) => Items(),
      transitionDuration: Duration(milliseconds: 500),
      transitionsBuilder: (context, animation, secondaryAnimation, child) {
        var begin = Offset(1.0, 0.0);
        var end = Offset(0.0,0.0);
        var curve = Curves.decelerate;
        var tween = Tween(begin: begin, end: end).chain(CurveTween(curve: curve));

        return SlideTransition(
          position: animation.drive(tween),
          child: child,
        );
      },
    );
  }
  groupsList(gr,pTag){
    return GridView.builder(
      physics: NeverScrollableScrollPhysics(),
      shrinkWrap: true,
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3),
      itemCount: gr.length,
      itemBuilder: (context, position){
        return GestureDetector(
          onTap: (){
            tag = int.parse('1$pTag$position');
            studentInfo['name']=gr[position]['name'];
            studentInfo['num']=gr[position]['num'];
            Navigator.push(context,itemRoute());
          },
          child: Hero(
            tag: 'stuHero1$pTag$position',
            child:Material(
              child:Container(
              margin: EdgeInsets.all(5),
              padding: EdgeInsets.all(10),
              decoration: BoxDecoration(
                border: Border.all(width: 2,color:Colors.lightBlue[700]),
                color: Colors.lightBlue[50],
                borderRadius: BorderRadius.circular(10),
              ),
              child: Text('${gr[position]['name']}\n${gr[position]['num']}',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.bold,
                  color: Colors.lightBlue[700]
                ),
              ),
            )
          )
          )
        );
      },
    );
  
  }

  students(){
    if(selectedTerm == null){
      return Center(
        child: Text('لطفا یک ترم را انتخاب کنید'),
      );
    }
    else{
      return FutureBuilder(
        builder: (context, snap) {
          if(snap.connectionState == ConnectionState.none){
            return Container(
              padding: EdgeInsets.all(100),
              child: Text('اتصال برقرار نیست'),
            );
          }else if(snap.connectionState == ConnectionState.waiting){
            return Container(
              padding: EdgeInsets.all(100),
              child: Text('لطفا صبر کنید'),
            );
          }else if(!snap.hasError && snap.hasData && snap.data.statusCode == 200){
            groups = jsonDecode(utf8.decode(snap.data.bodyBytes));
            return Container(
              child: ListView.separated(
                shrinkWrap: true,
                itemCount: groups['groups'].length,
                itemBuilder: (context, position){
                  return Container(
                    padding: EdgeInsets.all(5),
                    child: groupsList(groups['groups'][position],position),
                  );
                },
                separatorBuilder: (BuildContext context, int index) {
                  return Divider();
                },
              )
            );
          }else{
            return Container(
              padding: EdgeInsets.all(100),
              child: Text('مشکل در دریافت دیتا ${snap.data.body.toString()}'),
            );
          }
        },
        future: getGroups(),
      );
    }
  }

  Future<http.Response> getTerms() async {
    return await http.post(
      "http://mylogbook.ir/app/terms",
      body:{
        'username':master['username'],
        // 'password':passwordController.text,
      }
    );
  }
  // TODO post selectedTerm
  Future<http.Response> getGroups() async {
    return await http.post(
      "http://mylogbook.ir/app/groups",
      body:{
        'term':selectedTerm.toString(),
        // 'password':passwordController.text,
      }
    );
  }

// @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: DefaultTabController(
//         length: 2,
//         child: NestedScrollView(
//           headerSliverBuilder: (BuildContext context, bool innerBoxIsScrolled) {
//             return <Widget>[
//               SliverAppBar(
//                 expandedHeight: 50.0,
//                 floating: false,
//                 pinned: true,
//                 flexibleSpace: FlexibleSpaceBar(
//                     centerTitle: true,
//                     title: Text("Collapsing Toolbar",
//                         style: TextStyle(
//                           color: Colors.white,
//                           fontSize: 16.0,
//                         )),
//                     background: Image.network(
//                       "https://images.pexels.com/photos/396547/pexels-photo-396547.jpeg?auto=compress&cs=tinysrgb&h=350",
//                       fit: BoxFit.cover,
//                     )),
//               ),
//               new SliverPadding(
//                 padding: new EdgeInsets.all(16.0),
//                 sliver: new SliverList(
//                   delegate: new SliverChildListDelegate([
//                     Container(
//                       width: double.infinity,
//                       height: 50,
//                       child: FutureBuilder(
//                         builder: (context, snap) {
//                           if (snap.connectionState==ConnectionState.none){
//                             return Container(
//                               child: Text('اتصال برقرار نیست.'),
//                             );
//                           }else if(snap.connectionState==ConnectionState.waiting){
//                             return Container(
//                               child: Text('منظتر باشید.'),
//                             );
//                           }else if(snap.hasData==null){
//                             return Container(
//                               child: Text('دیتایی وجود ندارد'),
//                             );
//                           }else if(snap.data.statusCode!=200){
//                             return Container(
//                               child: Text('error: ${snap.data.statusCode}'),
//                             );
//                           }else{
//                             terms = jsonDecode(snap.data.body);
//                             return termsList();
//                           }
//                         },
//                         future: getTerms(),
//                       ) 
//                     )
//                   ]),
//                 ),
//               ),
//             ];
//           },
//           body: students(),
          
//         ),
//       ),
//     );




  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.lightBlue[100],
      appBar: AppBar(
        backgroundColor: Colors.lightBlue,
        title:Text('${master['name']}')
      ),
      body:Container(
        color: Colors.lightBlue[100],
      child: Column(
        children: <Widget>[
          Container(
            width: double.infinity,
            height: 60,
            child: FutureBuilder(
              builder: (context, snap) {
                if(terms != null){
                  return Container(
                    // color: Colors.lightBlue[100],
                    child: termsList(),
                  );
                }
                else if (snap.connectionState==ConnectionState.none){
                  return Container(
                    child: Text('اتصال برقرار نیست.'),
                  );
                }else if(snap.connectionState==ConnectionState.waiting){
                  return Container(
                    child: Text('منظتر باشید.'),
                  );
                }else if(snap.hasData==null){
                  return Container(
                    child: Text('دیتایی وجود ندارد'),
                  );
                }else if(snap.data.statusCode!=200){
                  return Container(
                    child: Text('error: ${snap.data.statusCode}'),
                  );
                }else{
                  terms = jsonDecode(snap.data.body);
                  return Container(
                    // color: Colors.lightBlue[100],
                    child: termsList(),
                  );
                }
              },
              future: getTerms(),
            ) // terms(),
          ),
          Expanded(
            child: ClipRRect(
            
            borderRadius: BorderRadius.only(
              topLeft : const Radius.circular(30.0),
              topRight: const Radius.circular(30.0),
            ),
              child: Container(
                color: Colors.white,
                child: students(),
              ) 
            ) ,
          ),
        ],
      ),
    )
    );

  }
}


class Items extends StatefulWidget {
  @override
  _ItemsState createState() => _ItemsState();
}

class _ItemsState extends State<Items> {

  Future<http.Response> getItems() async {
    return await http.post(
      "http://mylogbook.ir/app/items",
      body:{
        'no':studentInfo['num'],
        // 'password':passwordController.text,
      }
    );
  }

    Future<http.Response> send() async {
    
    return await http.post(
      "http://mylogbook.ir/app/save",
      body:{
        'items':jsonEncode(items4send),
        'student': studentInfo['num']
        // 'password':passwordController.text,
      }
    );
  }

  static List<Widget> itemBuild(pos){
    
    List<Widget> thisItems = [];
    for (var i in items['items'][pos]['items']){
      i['plus'] = 0;
      thisItems.add(
        StatefulBuilder(
          builder: (ctx, setState){
            if (i['plus'] == 0)
            return ListTile(
              title: Text(i['name']),
              subtitle: Text('حداقل تعداد: ${i['min']}'),
              trailing: Text('${i['count']}'),
              onTap: (){
                setState((){
                  i['plus'] ++;
                  items4send['${i['id']}'] = '${i['plus']}';
                });
              },
            );
            return ListTile(
              title: Text(i['name']),
              subtitle: Text('حداقل تعداد: ${i['min']}'),
              trailing: Text('${i['plus']}+ ${i['count']}',style: TextStyle(
                color: Colors.blue[700]
              ),),
              onTap: (){
                setState((){
                  i['plus'] ++;
                  items4send['${i['id']}'] = '${i['plus']}';
                });
              },
              onLongPress: (){
                setState((){
                  i['plus'] --;
                  items4send['${i['id']}'] = '${i['plus']}';
                });
              },
            );

          },
        )
      );
    }
    return thisItems;
  }

  Container interItem(pos){
    return Container(
      child:  ExpansionTile(
          title: Text('${items['items'][pos]['name']}'),
          children: itemBuild(pos)
          )
    );
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.lightBlue,
        title: Text('فعالیت ها'),
      ),
      body: Container(
        child: Column(
          children: <Widget>[
            Container(
              width: MediaQuery.of(context).size.width,
              alignment: Alignment.center,
              child: Hero(
                tag: 'stuHero$tag',
                child:Material(
                  child: Container(
                  margin: EdgeInsets.all(5),
                  padding: EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    border: Border.all(width: 2,color:Colors.lightBlue[700]),
                    color: Colors.lightBlue[50],
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Text('${studentInfo['name']}\n${studentInfo['num']}',
                    softWrap: false,
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                      color: Colors.lightBlue[700]
                    ),
                  ),
                )
                ),
              )
            ),
            FutureBuilder(
              builder: (context, snap) {
                if (snap.connectionState==ConnectionState.none){
                  return Container(
                    child: Text('اتصال برقرار نیست.'),
                  );
                }else if(snap.connectionState==ConnectionState.waiting){
                  return Container(
                    child: Text('لطفا صبر کنید.'),
                  );
                }else if(snap.hasData==null){
                  return Container(
                    child: Text('دیتایی وجود ندارد'),
                  );
                }else if(snap.data.statusCode!=200){
                  return Container(
                    child: Text('error: ${snap.data.statusCode}'),
                  );
                }else{
                  items = jsonDecode(snap.data.body);
                  return Expanded(
                    child: ListView.builder(
                    itemCount: items['items'].length+1,
                    itemBuilder: (ctx, pos){
                      if (pos == items['items'].length){
                        return Container(
                          child: FlatButton(
                            onPressed: (){
                              if(items4send.isEmpty){
                                  Scaffold.of(context).showSnackBar(SnackBar(
                                    content: Text("چیزی برای ثبت نیست!!"),
                                    duration: Duration(seconds: 1),
                                  ));
                                }else{
                                  send().then((s){                               
                                    if(s.body == 'ok'){
                                      items4send.clear();
                                      Scaffold.of(context).showSnackBar(SnackBar(
                                        content: Text("با موفقیت ثبت شد"),
                                      ));
                                      setState(() {
                                      });
                                    }else{
                                      Scaffold.of(context).showSnackBar(SnackBar(
                                        content: Text("مشکلی وجود دارد. دوباره امتحان کنید."),
                                      ));
                                    }
                                  });
                                }
                              },

                            // color: Colors.white,
                            child: Container(
                              decoration: BoxDecoration(
                                color: Colors.lightBlue,
                                borderRadius: BorderRadius.circular(5)
                              ),
                              width: MediaQuery.of(context).size.width/3,
                              height: 33,
                              child: Text('ثبت',
                                textAlign: TextAlign.center,
                                style: TextStyle(
                                  color: Colors.white,
                                  fontSize: 20
                                ),
                                ),
                            )
                          ),
                        );
                      }
                        return interItem(pos);
                    
                    }),
                  );
              
                }
              },
              future: getItems(),
            ),
          ],
        ),
      ),
    );
  }
}




class Fernet {

  String decrypt(str){

    final key = en.Key.fromUtf8('12345678901234567890123456789012');
    final b64key = en.Key.fromUtf8(base64Url.encode(key.bytes));
    final fernet = en.Fernet(b64key);
    final encrypter = en.Encrypter(fernet);
    final decrypted = encrypter.decrypt64(str);

    return jsonDecode(decrypted.replaceAll("'", "\""));

  }

  String encrypt(str){

    final key = en.Key.fromUtf8('12345678901234567890123456789012');
    final b64key = en.Key.fromUtf8(base64Url.encode(key.bytes));
    final fernet = en.Fernet(b64key);
    final encrypter = en.Encrypter(fernet);
    final encrypted = encrypter.encrypt(str);

    return encrypted.toString();
  }

}















///////////////////////////////
///
/// Old code 
///
//////////////////////////////
class StudentList extends StatefulWidget {
  @override
  _StudentListState createState() => _StudentListState();
}

class _StudentListState extends State<StudentList> {
  
  stuItem(myModel,stu){
    return Container(
      child: FlatButton(
        child: Text(stu['name']),
        onPressed: (){
          items=stu['items'];
          myModel.doSomething();
          },
      )
    );
  }
  
  item(myModel,intershipName){
    var term =intershipName['term'];
    return Column(
      children: <Widget>[
        Text(intershipName['name']+' '+'$term'),
        GridView.builder(
          physics: NeverScrollableScrollPhysics(),
          shrinkWrap: true,
          padding: EdgeInsets.all(30),
          itemCount: intershipName['students'].length, // Intership.students.length()
          itemBuilder: (context,position){
            return stuItem(myModel, intershipName['students'][position]);
          },
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3),
        ), 
      ]
    );
  }


  @override
  Widget build(BuildContext context) {
    var interships = [];
    if (response["status"]=="ok"){
      interships = response["interships"];
    }
    return Consumer<MyModel>(
      builder: (context,myModel,child){
        return ListView.builder(
        shrinkWrap: true,
        itemCount: interships.length, // Intership.length
        itemBuilder: (contex,position){
          return item(myModel, interships[position]);
        },
      ) ;
      },
      
    );
    
    
  }
}



class ItemPage extends StatefulWidget {
  @override
  _ItemPageState createState() => _ItemPageState();
}

class _ItemPageState extends State<ItemPage> {



  @override
  Widget build(BuildContext context) {
    return Container(
      child: Consumer<MyModel>(
        builder:(context,myModel,child){
          return ListView.builder(
            itemCount: items.length,
            itemBuilder: (context,position){
              var min = items[position]['min'];
              var count = items[position]['count'];
          return Container(
            child: ListTile(
              title: Text(items[position]['name']),
              subtitle: Text('حداقل: $min'),
              trailing: Text('$count'),
            )
          );
        },
      );
        },
        ) 
    );
  }
}


class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}


class MyModel with ChangeNotifier{ 
  String someValue = 'Hello';
  void doSomething() {
    someValue = 'Goodbye';
    print(someValue);
    notifyListeners();

  }
}


class MyFx {
  
  void get_terms(){

  }
}




















class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }
  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.display1,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
