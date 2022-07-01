from manim import *

class Square(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Tex('(0, 0)').next_to(dot, DOWN)
        tip_text = Tex('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)

        square = Rectangle(stroke_color=RED, fill_color=GREEN, fill_opacity=0.8, height=1, width=1)
        circle = Circle(radius=2, stroke_color=WHITE, fill_color=BLUE, fill_opacity=0.8)

        self.play(GrowFromCenter(square), run_time=2)
        self.play(Rotating(square, about_point=[0, 0, 0]), run_time=1.5)
        self.play(Transform(square, circle), run_time=4)

                # Create Text objects
        first_line = Text('Lag KULE animasjoner')
        second_line = Text('ved bruk av Manim')
        third_line = Text('Prøv selv da vel ;)', color=RED)

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, third_line), FadeOut(second_line))
        self.wait(2)
        self.play(FadeOut(square), FadeOut(third_line), FadeOut(dot),
                  FadeOut(arrow), FadeOut(numberplane), FadeOut(origin_text),
                  FadeOut(tip_text))

        axes = Axes(
            x_range=[-3, 3],
            y_range=[-5, 5],
            axis_config={"color": BLUE}
            )

        # Create Graph
        graph = axes.get_graph(lambda x: x**2, color=WHITE)
        graph_label = axes.get_graph_label(graph, label='x^{2}')

        graph2 = axes.get_graph(lambda x: x**3, color=WHITE)
        graph_label2 = axes.get_graph_label(graph2, label='x^{3}')

        # Display graph
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.wait(1)
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(graph_label))

        end_text = Tex(r'$\cdot\oint\Gamma_{\mu}\cdot$').scale(5)
        self.play(Write(end_text), run_time=3)
