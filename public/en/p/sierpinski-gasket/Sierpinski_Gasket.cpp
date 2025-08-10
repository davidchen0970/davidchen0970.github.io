#include <GL/glut.h>
#include <stdio.h>
#include <math.h>
#include <Windows.h>
#include <iostream>

using namespace std;
GLfloat angle = 0.0f;
GLfloat arm_first_angle = 0.79, arm_second_angle = 2.36;
int base = -40;


void first_display()
{
	typedef GLfloat point2[2];            // arbitrary triangle,任意三角形 
	point2 vertices[3] = { {0.0,0.0}, {250.0,500.0}, {500.0,0.0} };
	/* any desired initial point */
	point2 p = { 75.0,75.0 };
	for (int i = 0; i < 5000; i++)
	{
		/* pick a random vertex from 0,1,2 */
		int j = rand() % 3;
		/* compute new point */
		p[0] = (p[0] + vertices[j][0]) / 2.0;
		p[1] = (p[1] + vertices[j][1]) / 2.0;
		// cout << '(' << p[0] << ',' << p[1] << ',' << 0 << ')' << endl;
		/* display new point */
		glBegin(GL_POINTS);
		glVertex2fv(p);
		glEnd();
	}
	glFlush();
}

void init_render()
{
	glMatrixMode(GL_PROJECTION);			        //要用GL_PROJECTION模式才可以改視窗
	glLoadIdentity();
	glOrtho(-100, 600, -100, 600, -100, 600); //將視角的邊界設為(三維右下:(-100,-100,600),左上:(600,600,-100))
	glMatrixMode(GL_MODELVIEW);
}


int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);           //視窗大小
	glutCreateWindow("CH2");                //視窗的名稱
	glutDisplayFunc(first_display);         //繪製三維世界的內容
	init_render();                          //繪製一個三維世界
	glutMainLoop();                         //開始執行程式
}