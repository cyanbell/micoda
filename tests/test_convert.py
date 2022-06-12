from unittest import TestCase
import tempfile

from fugue import convert, convert_from_file


class ConvertTestCase(TestCase):
    def setUp(self) -> None:
        self.text = """# Title

> This is a blockquote.

## Ordered list

1. **First**
2. *Second*
3. Third

## Code

- Code block:

    ```python
    def main() -> None:
        print("Hello, world.")
    ```

- Span of code:

    `print(Hello, world.)`

## Links and Image

### Links

Go to [Github](https://github.com).  
Go to [Google][Google].

[Google]: https://www.google.com

---

### Image

Rust logo:

![Rust](https://www.rust-lang.org/static/images/rust-logo-blk.svg)

""" # noqa

        self.html = """<h1>Title</h1>
<blockquote>
<p>This is a blockquote.</p>
</blockquote>
<h2>Ordered list</h2>
<ol>
<li><strong>First</strong></li>
<li><em>Second</em></li>
<li>Third</li>
</ol>
<h2>Code</h2>
<ul>
<li>
<p>Code block:</p>
<pre><code class="language-python">def main() -&gt; None:
    print(&quot;Hello, world.&quot;)
</code></pre>
</li>
<li>
<p>Span of code:</p>
<p><code>print(Hello, world.)</code></p>
</li>
</ul>
<h2>Links and Image</h2>
<h3>Links</h3>
<p>Go to <a href="https://github.com">Github</a>.<br />
Go to <a href="https://www.google.com">Google</a>.</p>
<hr />
<h3>Image</h3>
<p>Rust logo:</p>
<p><img src="https://www.rust-lang.org/static/images/rust-logo-blk.svg" alt="Rust" /></p>
""" # noqa

        return super().setUp()

    def test_convert(self) -> None:
        self.assertEqual(
            self.html,
            convert(self.text)
        )

    def test_convert_from_file(self) -> None:
        """
        test convert markdown file to html.
        write something into temp file, by `tempfile` standard library .
        """
        with tempfile.NamedTemporaryFile("w") as file:
            file.write(self.text)
            file.seek(0)
            self.assertEqual(
                self.html,
                convert_from_file(file.name)
            )