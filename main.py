from manim import *
import math

def create_box(text):
    result = VGroup()
    box = Square(side_length=0.75, stroke_width=0)
    result.add(box,Text(text, font_size=24).move_to(box.get_center()))
    return result

class Pascal(Scene):
    def construct(self):
        title = Text("Pascal's Triangle", font_size=36).to_edge(UP)
        subtitle1 = Tex(R"$\binom{n}{k} = \frac{n!}{k!(n-k)!} = \binom{n-1}{k-1} + \binom{n-1}{k}$", font_size=36).shift(UP*0.75)
        subtitle2 = Tex(R"$\sum_{i=0}^{n} \binom{n}{i} = 2^n$", font_size=36).shift(DOWN*0.75)
        self.play(Write(title))
        self.play(Write(subtitle1), Write(subtitle2))
        self.wait(0.5)
        self.play(FadeOut(subtitle1),FadeOut(subtitle2))
        self.wait(0.5)
        self.play(title.animate.to_corner(UL), run_time=0.75)
        sub1 = Tex(R"$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$", font_size=30).next_to(title, DOWN)
        sub2 = Tex(R"$\sum_{i=0}^{n} \binom{n}{i} = 2^n$", font_size=30).next_to(title, DOWN)
        self.wait(0.5)
        row = 8
        pyramid = VGroup()
        sums = VGroup()
        for i in range(0,row+1):
            layer = VGroup()
            ss = ""
            for j in range(i+1):
                if j != 0:
                    ss = ss + " + "
                textbox = create_box(str(math.comb(i,j)))
                ss = ss + str(math.comb(i,j))
                layer.add(textbox)
            layer.arrange(RIGHT, buff = 0)
            pyramid.add(layer)
            sum_box = create_box(ss+" = "+str(2**i))
            sums.add(sum_box)
        pyramid.arrange(DOWN, center=True, buff = 0)
        sums.arrange(DOWN, center=True, buff=0)
        edges = VGroup(*[
            VGroup(row[0],row[-1]) for row in pyramid
        ])
        self.play(Write(edges))
        self.wait()
        self.play(
            FadeTransform(VGroup(title).copy(), sub1), run_time = 0.75
        )
        rec = SurroundingRectangle(pyramid[1],buff=0)
        self.play(Create(rec))
        self.play(
            FadeTransform(VGroup(pyramid[1],rec).copy(), pyramid[2][1]), run_time = 0.75
        )
        speed = [0.5, 0.75]
        for i in range(2,row):
            r = pyramid[i]
            if i == 4:
                self.play(Uncreate(rec), run_time=0.3)
            for j in range(i):
                act_row = r[j:j+2]
                if i < 4:
                    self.play(
                        Transform(rec, SurroundingRectangle(act_row,buff=0), run_time = 0.5)
                    )
                    self.play(
                        FadeTransform(VGroup(act_row,rec).copy(), pyramid[i+1][j+1]), run_time = 0.75
                    )
                else:
                    self.play(
                        FadeTransform(VGroup(act_row).copy(),pyramid[i+1][j+1]), run_time = 0.3
                    )
        self.play(Transform(sub1,sub2))
        self.wait()
        for i, layer in enumerate(pyramid):
            self.play(Transform(layer,sums[i]), run_time=0.75)
        self.wait()
        self.play(FadeOut(pyramid),FadeOut(title),FadeOut(sub1),FadeOut(sub2))
        self.wait(2)