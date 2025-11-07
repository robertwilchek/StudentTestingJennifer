using System;

namespace HelloWorld
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello world");
            string file = "hello1.txt";
            string content = "Hello World";
            File.WriteAllText(file, content);
        }
    }
}
