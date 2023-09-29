#include <stdio.h>
#include<conio.h>
int main()
{
  int selection ,aa,bb,cc;
  char a,b,c,d,e,f,g,h,i,sel,sel2;
  start:
  a = 'a', b = 'b', c = 'c', d = 'd', e = 'e', f = 'f', g = 'g',h = 'h', i = 'i';
  printf("     |     |    \n");
  printf("  %c  |  %c  |  %c\n", a, b, c);
  printf("     |     |    \n");
  printf("-----------------\n");
  printf("     |     |    \n");
  printf("  %c  |  %c  |  %c\n", d, e, f);
  printf("     |     |    \n");
  printf("-----------------\n");
  printf("     |     |    \n");
  printf("  %c  |  %c  |  %c\n", g, h, i);
  printf("     |     |    \n");
  printf("Just enter the number where you want to insert\n");
  for ( aa = 0; aa <= 10; aa++)
  {
    for ( bb = 0; bb <= 10; bb++)
    {
      printf("player 1:");
      scanf("%c", &sel);
      if (sel == 'a') {
        if (a == 'X' || a == '0') {
          printf("invalid move\n");
        } else {
        	system("cls");
          a = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if(a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') 
              {
                 printf("player 1 wins");
                 goto end;
              }
              
          break;
        }
      }

      if (sel == 'b') {
        if (b == 'X' || b == '0') {
          printf("invalid move\n");
        } else {
        	system("cls");
          b = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
            goto end;
          }
          
          break;
        }
      }

      if (sel == 'c') {
        if (c == 'X' || c == '0') {
          printf("invalid move\n");
        } else {
        	system("cls");
          c = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
            goto end;
          }
          
          break;
        }
      }

      if (sel == 'd') {
        if (d == 'X' || d == '0') {
          printf("invalid move\n");
        } else {
        	system("cls");
          d = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
            goto end;
          }
          
          break;
        }
      }

      if (sel == 'e') {
        if (e == 'X' || e == '0') {
          printf("invalid move\n");
        } else {
        	system("cls");
          e = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
            goto end;
          }
          
          break;
        }
      }
      if (sel == 'f') {
         if (f == 'X' || f == '0') {
          printf("invalid move\n");
        } else {
        	system("cls");
          f = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
            goto end;
          }
         
           break;
        }
      }
      if (sel == 'g') {
        if (g == 'X' || g == '0')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          g = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
             goto end;
          }
         
           break;
        }
      }
      if (sel == 'h') {
         if (h == 'X' || h == '0')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          h = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
            goto end;
          }
          
           break;
        }
      }
      if (sel == 'i') {
         if (i == 'X' || i == '0')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          i = '0';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == '0' && b == '0' && c == '0' ||
              d == '0' && e == '0' && f == '0' ||
              g == '0' && h == '0' && i == '0' ||
              a == '0' && d == '0' && g == '0' ||
              b == '0' && e == '0' && h == '0' ||
              c == '0' && f == '0' && i == '0' ||
              a == '0' && e == '0' && i == '0' ||
              g == '0' && e == '0' && c == '0') {
            printf("player 1 wins");
            goto end;
          }
          
           break;
        }
      }
    }
    //}
    for( cc = 0; cc <= 10; cc++)
     {
      printf("player 2:");
      scanf("%c", &sel2);
      if (sel2 == 'a') {
         if (a == '0' || a == 'X')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          a = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
             goto end;
          }
         
           break;
        }
      }
      if (sel2 == 'b') {
         if (b == '0' || b == 'X')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          b = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
             goto end;
          }
         
           break;
        }
      }
      if (sel2 == 'c') {
         if (c == '0' || c == 'X')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          c = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
             goto end;
          }
          
           break;
        }
      }
      if (sel2 == 'd') {
         if (d == '0' || d == 'X')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          d = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
             goto end;
          }
          
           break;
        }
      }
      if (sel2 == 'e') {
         if (e == '0' || e == 'X')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          e = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
            goto end;
          }
          
           break;
        }
      }
      if (sel2 == 'f') {
         if (f == '0' || f == 'X')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          f = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
            goto end;
          }
          
           break;
        }
      }
      if (sel2 == 'g') {
         if (g == '0' || g == 'X')
        {
            printf("invalid move\n");
        }
          else {
          	system("cls");
          g = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
             goto end;
          }
           break;
        }
      }
      if (sel2 == 'h') {
         if (h == '0' || h == 'X')
        {
            printf("invalid move\n");
        }
          else {
          system("cls");
          h = 'X';
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
             goto end;
          }
           break;
        }
      }
      if (sel2 == 'i') {
         if (i == '0' || i == 'X')
        {
            printf("invalid move\n");
        }
          else {
          i = 'X';
          system("cls");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", a, b, c);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", d, e, f);
          printf("     |     |    \n");
          printf("-----------------\n");
          printf("     |     |    \n");
          printf("  %c  |  %c  |  %c\n", g, h, i);
          printf("     |     |    \n");
          if (a == 'X' && b == 'X' && c == 'X' ||
              d == 'X' && e == 'X' && f == 'X' ||
              g == 'X' && h == 'X' && i == 'X' ||
              a == 'X' && d == 'X' && g == 'X' ||
              b == 'X' && e == 'X' && h == 'X' ||
              c == 'X' && f == 'X' && i == 'X' ||
              a == 'X' && e == 'X' && i == 'X' ||
              g == 'X' && e == 'X' && c == 'X') {
            printf("player 2 wins");
            goto end;
          }
          
           break;
        }
      }
    }
  }
    end:
    {
        printf("\nYOU WANNA PLAY AGAIN? \nenter 1 to play or 0 to stop");
        scanf("%d",&selection);
        if(selection == 1)
        {
            goto start;
        }
        else
        {
            printf("Thank you for playing:");
        }
    }
  return 0;
}