import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "BoxVinil",
      theme: ThemeData(
        scaffoldBackgroundColor: const Color.fromARGB(255, 24, 24, 24),
      ),
      home: WidgetLogin(),
    );
  }
}

// Classe da Tela de Login
class WidgetLogin extends StatefulWidget {
  const WidgetLogin({super.key});

  @override
  State<WidgetLogin> createState() => _WidgetLoginState();
}

class _WidgetLoginState extends State<WidgetLogin> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: const EdgeInsets.all(50),

        // Imagem (Logo)
        child: ListView(
          children: <Widget>[
            const SizedBox(
              height: 100,
            ),
            SizedBox(
                width: 280, height: 216, child: Image.asset("assets/logo.png")),
            const SizedBox(
              height: 80,
            ),

            // TextFormField E-mail
            TextFormField(
              style: const TextStyle(color: Colors.black),
              obscureText: false,
              decoration: InputDecoration(
                  filled: true,
                  fillColor: Colors.white,
                  contentPadding:
                      const EdgeInsets.fromLTRB(25.0, 10.0, 25.0, 1.0),
                  hintText: "E-mail",
                  hintStyle: const TextStyle(color: Colors.grey),
                  border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(10))),
            ),
            const SizedBox(
              height: 30,
            ),

            // TextFormField Senha
            TextFormField(
              style: const TextStyle(color: Colors.black),
              obscureText: true,
              decoration: InputDecoration(
                  filled: true,
                  fillColor: Colors.white,
                  contentPadding:
                      const EdgeInsets.fromLTRB(25.0, 10.0, 25.0, 1.0),
                  hintText: "Senha",
                  hintStyle: const TextStyle(color: Colors.grey),
                  border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(10))),
            ),
            const SizedBox(
              height: 30,
            ),

            // Button Entrar
            Container(
              height: 41.0,
              alignment: Alignment.centerLeft,
              decoration: BoxDecoration(
                color: const Color.fromARGB(255, 50, 205, 50),
                borderRadius: BorderRadius.circular(10),
              ),
              child: SizedBox.expand(
                child: TextButton(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: const [
                      Text(
                        "Entrar",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                            fontSize: 18),
                      )
                    ],
                  ),
                  // Adcionar function que redireciona a tela principal
                  onPressed: () {},
                ),
              ),
            ),
            const SizedBox(
              height: 17,
            ),

            // Redireciona para page cadastro
            Container(
              height: 20,
              alignment: Alignment.centerLeft,
              child: SizedBox.expand(
                child: TextButton(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: const <Widget>[
                      Text.rich(
                        TextSpan(
                            text: "Não possui uma conta? ",
                            style: TextStyle(color: Colors.white, fontSize: 16),
                            children: <TextSpan>[
                              TextSpan(
                                  text: "Cadastre-se",
                                  style: TextStyle(
                                      decoration: TextDecoration.underline))
                            ]),
                      ),
                    ],
                  ),
                  // Adicionar fuction que redireciona a page cadastro
                  onPressed: () {},
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
