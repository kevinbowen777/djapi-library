Add book list
=============

Template for adding a list of books to djapi-library Django application

.. code-block:: console

    book = Book.objects.create(
        title="",
        author="",
        pages=xxx,
        publisher="",
        pubdate="",
        price="",
        isbn="",
        isbn="",
    )

Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample book list
----------------

.. code-block:: console

    book = Book.objects.create(
        title="Brave New World",
        subtitle="",
        author="Aldous Huxley",
        pages=268,
        publisher="HarperPerennial / Perennial Classics",
        pubdate="1932-09-01",
        price="19.95",
        isbn="0060929871",
    )

    Book.objects.create(
        title="Django for Beginners",
        subtitle="Learn web development with Django",
        author="William S. Vincent",
        pages=262,
        publisher="Lean Publishing",
        pubdate="2018-02-02",
        price="39.95",
        isbn="1735467200",
    )

    Book.objects.create(
        title="Django for APIs",
        subtitle="Build web APIs with Python & Django",
        author="William S. Vincent",
        pages=155,
        publisher="Lean Publishing",
        pubdate="2018-06-18",
        price="49.95",
        isbn="1093633948",
    )

    Book.objects.create(
        title="Django for Professionals",
        subtitle="Production websites with Python & Django",
        author="William S. Vincent",
        pages=406,
        publisher="Lean Publishing",
        pubdate="2019-07-20",
        price="19.95",
        isbn="31735467235",
    )

    Book.objects.create(
        title="Atoms, Metaphors and Paradoxes",
        subtitle="Niels Bohr and the Construction of a New Physics",
        author="Sandro Petruccioli",
        pages=252,
        publisher="Cambridge University Press",
        pubdate="2006-11-23",
        price="39.95",
        isbn="0521031885",
    )

    Book.objects.create(
        title="Luce elettricità magnetismo",
        subtitle="",
        author="Sandro Petruccioli",
        pages=214,
        publisher="Istituto della Enciclopedia Italiana",
        pubdate="2012-09-25",
        price="79.95",
        isbn="9781234567897",
    )

    Book.objects.create(
        title="The Structure of Scientific Revolutions",
        subtitle="",
        author="Thomas Kuhn",
        pages=226,
        publisher="University of Chicago Press",
        pubdate="1962-03-29",
        price="29.95",
        isbn="0226458083",
    )

    Book.objects.create(
        title="Black-Body Theory and the Quantum Discontinuity, 1894-1912",
        subtitle="",
        author="Thomas Kuhn",
        pages=298,
        publisher="University of Chicago Press",
        pubdate="1978-06-16",
        price="49.95",
        isbn="0226458008",
    )

    Book.objects.create(
        title="Capitalist Realism",
        subtitle="Is There No Alternative?",
        author="Mark Fisher",
        pages=181,
        publisher="Zero Books",
        pubdate="2009-11-27",
        price="12.95",
        isbn="1846943175",
    )

    Book.objects.create(
        title="Ghosts of My Life",
        subtitle="Writings on Depression, Hauntology and Lost Futures",
        author="Mark Fisher",
        pages=245,
        publisher="Zero Books",
        pubdate="2014-05-30",
        price="26.95",
        isbn="1846253175",
    )

    Book.objects.create(
        title="The Conquest of Bread",
        subtitle="",
        author="Pyotr Kropotkin",
        pages=320,
        publisher="Ardent Press",
        pubdate="1892-06-06",
        price="9.95",
        isbn="1904859100",
    )

    Book.objects.create(
        title="Anarchism",
        subtitle="A Collection of Revolutionary Writings",
        author="Pyotr Kropotkin",
        pages=307,
        publisher="Dover Publications",
        pubdate="1927-01-04",
        price="8.95",
        isbn="978048641955",
    )

    Book.objects.create(
        title="My Mother: Demonology",
        subtitle="",
        author="Kathy Acker",
        pages=236,
        publisher="Random House Publishing",
        pubdate="1932-09-01",
        price="19.95",
        isbn="0517144867",
    )

    Book.objects.create(
        title="Blood and Guts in High School",
        subtitle="",
        author="Kathy Acker",
        pages=268,
        publisher="Grove Press",
        pubdate="1985-01-11",
        price="27.95",
        isbn="080213193X",
    )

    Book.objects.create(
        title="Dubliners",
        subtitle="",
        author="James Joyce",
        pages=207,
        publisher="Oxford University Press",
        pubdate="1914-06-16",
        price="9.95",
        isbn="0192839993",
    )

    Book.objects.create(
        title="Ulysses",
        subtitle="",
        author="James Joyce",
        pages=783,
        publisher="Vintage",
        pubdate="1922-02-02",
        price="16.95",
        isbn="2132546652001",
    )

    Book.objects.create(
        title="Eyeless in Gaza",
        subtitle="",
        author="Aldous Huxley",
        pages=268,
        publisher="Penguin Classics",
        pubdate="1927-09-01",
        price="9.95",
        isbn="0192828893",
    )

    Book.objects.create(
        title="Programming Python",
        subtitle="",
        author="Mark Lutz",
        pages=768,
        publisher="O'Reilly Publishing",
        pubdate="2005-08-01",
        price="59.95",
        isbn="0967144867",
    )

    Book.objects.create(
        title="Test-Driven Development with Python",
        subtitle="",
        author="Harry J.W. Percival",
        pages=268,
        publisher="O'Reilly Publishing",
        pubdate="2011-03-29",
        price="59.99",
        isbn="2317144867",
    )

    Book.objects.create(
        title="Two Scoops of Django 3.x",
        subtitle="",
        author="Daniel Feldroy",
        pages=222,
        publisher="Lean Publishing",
        pubdate="2019-04-01",
        price="27.99",
        isbn="4917144867",
    )
