import plotly.express as px

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]

# Write your code here

graph = { "Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
    "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
    "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
    "Chile": ["Argentina", "Bolivia", "Peru"],
    "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
    "Ecuador": ["Colombia", "Bolivia", "Peru"],
    "Falkland Islands": [],
    "Guyana": ["Brazil", "Suriname", "Venezuela"],
    "Paraguay": ["Argentina", "Bolivia", "Brazil"],
    "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"],
    "Suriname": ["Brazil", "Guyana"],
    "Uruguay": ["Argentina", "Brazil"],
    "Venezuela": ["Brazil", "Colombia", "Guyana"] }


def sortCountriesByNeighbors():

    tmpCountries = {}

    for country in countries:
        tmpCountries.update({country: len(graph[country])})
    tmpCountries = list(sorted(tmpCountries.items(), key=lambda kv: kv[1]))
    countries.clear()

    i = len(tmpCountries) - 1

    while i > -1:
        countries.append(tmpCountries[i][0])
        i -= 1


def isColorCorrect(coloredMap):

    for node in graph:
        edges = (graph[node])
        colorOfNode = coloredMap[node]

        for edge in edges:
            colorOfEdge = coloredMap[edge]

            if colorOfNode == colorOfEdge:
                return False

    return True


def coloringMap():

    color_index = 0
    country_index = 0
    counter = 0
    ret = True

    while country_index < len(countries):

        if counter == len(colors):
            print("Unsolved Problem")
            ret = False
            break
        before = country_index
        clrMap.update({countries[country_index]: colors[color_index]})
        if not isColorCorrect(clrMap):
            country_index -= 1
        if color_index < 3:
            color_index += 1
        else:
            color_index = 0
        country_index += 1
        if before == country_index:
            counter += 1
        else:
            counter = 0

    return ret


# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.


def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    if isColorCorrect(colormap_test):
        print("colormap_test is RIGHT colored.")

    else:
        print("colormap_test is FALSE colored.")

    sortCountriesByNeighbors()
    clrMap = {}

    for i in range(len(countries)):
        clrMap.update({countries[i]: f"emptyColor{i}"})

    if coloringMap():
        print("clrMap is RIGHT colored.")
        plot_choropleth(colormap=clrMap)
    else:
        print("clrMap is FALSE colored.")
