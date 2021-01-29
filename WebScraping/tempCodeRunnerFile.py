    results = div.select("i")

                    # Check if we have found a result
                    if (len(results) >= 1):

                        # Print the title
                        h3 = results[0]
                        return(h3.get_text())
                    else:
                        pass