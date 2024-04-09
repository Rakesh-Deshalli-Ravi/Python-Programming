# Name: Rakesh Deshalli Ravi
# Date: 1 Nov 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/yHgLydfcdYQ
# Assignment 0802: SpotiPy

import pandas as pd

# Function to summarize genres and their statistics
def summarize_genres(genres, artists_df):
    """
    Summarize genre statistics.

    Args:
        genres (list): List of genres to summarize.
        artists_df (pd.DataFrame): DataFrame containing artist data.

    Returns:
        pd.DataFrame: DataFrame summarizing genre statistics.
    """
    genre_counts = []
    genre_avg_followers = []
    
    for genre in genres:
        # Filter artists by genre and calculate counts and average followers
        genre_artists = artists_df[artists_df['genres'].str.contains(genre, case=False, na=False)]
        genre_counts.append(len(genre_artists))
        genre_avg_followers.append(genre_artists['followers'].mean())
    
    # Create a DataFrame to summarize genre statistics
    summary_df = pd.DataFrame({'genre': genres, 'total N': genre_counts, 'Av. followers': genre_avg_followers})
    return summary_df

# Function to find variants of a genre within the artist dataset
def get_genre_variants(genre, artists_df):
    """
    Find variants of a genre within the artist dataset.

    Args:
        genre (str): The genre to find variants of.
        artists_df (pd.DataFrame): DataFrame containing artist data.

    Returns:
        list: List of variants of the specified genre.
    """
    # Get all unique genres and filter variants of the specified genre
    all_genres = artists_df['genres'].str.split(', ').explode().unique()
    variants = [g for g in all_genres if genre in g]
    return variants

# Function to summarize an artist's performance based on tracks
def summarize_artist_performance(name, artists_df, tracks_df):
    """
    Summarize an artist's performance based on tracks.

    Args:
        name (str): The name of the artist to summarize.
        artists_df (pd.DataFrame): DataFrame containing artist data.
        tracks_df (pd.DataFrame): DataFrame containing track data.

    Returns:
        None
    """
    # Filter tracks by artist and calculate various performance metrics
    artist_tracks = tracks_df[tracks_df['id_artists'].str.contains(artists_df[artists_df['name'] == name]['id'].values[0])]
    num_tracks = len(artist_tracks)
    solo_tracks = len(artist_tracks[artist_tracks['id_artists'].str.count(',') == 0])
    collaborative_tracks = num_tracks - solo_tracks
    avg_popularity_total = artist_tracks['popularity'].mean()
    avg_popularity_solo = artist_tracks[artist_tracks['id_artists'].str.count(',') == 0]['popularity'].mean()
    avg_popularity_collaborative = artist_tracks[artist_tracks['id_artists'].str.count(',') > 0]['popularity'].mean()
    num_collaborators = artist_tracks[artist_tracks['id_artists'].str.contains(artist_tracks['id_artists'].values[0])]['id_artists'].str.split(', ').explode().nunique()
    print(f"\nArtist: {name}")
    print("Number of Tracks:", num_tracks)
    print("Number of Solo Tracks:", solo_tracks)
    print("Number of Collaborative Tracks:", collaborative_tracks)
    print("Average Popularity (Total):", avg_popularity_total)
    print("Average Popularity (Solo):", avg_popularity_solo)
    print("Average Popularity (Collaborative):", avg_popularity_collaborative)
    print("Number of Collaborators:", num_collaborators)

    # Check if the popularity metrics are similar or different
    if abs(avg_popularity_solo - avg_popularity_collaborative) < 2 and (avg_popularity_total - avg_popularity_solo) < 2 and (avg_popularity_total - avg_popularity_collaborative) < 2:
        print("The average popularity of total, solo, and collaborative tracks is similar.")
    else:
        print("The average popularity of total, solo, and collaborative tracks is different.")

# Function to organize the main logic
def main():
    """
    Main function to run the analysis and summary of data.
    """
    # Read artist and track data from CSV files
    artists_df = pd.read_csv('artists.tsv', sep='\t')
    tracks_df = pd.read_csv('tracks.tsv', sep='\t')

    # Find the artist with the maximum number of followers
    max_followers_artist = artists_df.loc[artists_df['followers'].idxmax()]
    print("Artist with the maximum number of followers:")
    print("Followers: ", artists_df['followers'].idxmax())
    print("Name:", max_followers_artist['name'])
    print("Genre:", max_followers_artist['genres'])

    # Find the most productive artist based on the number of tracks
    most_productive_artist = tracks_df['id_artists'].str.split(', ').explode().value_counts().idxmax()
    print("\nMost productive artist:")
    print("Name:", artists_df.loc[artists_df['id'] == most_productive_artist, 'name'].values[0])

    # List of genres to summarize
    genres_to_summarize = ['pop', 'hip hop', 'rock', 'metal', 'jazz', 'blues', 'country', 'folklore']
    genre_summary = summarize_genres(genres_to_summarize, artists_df)
    print("\nGenre Summary:")
    print(genre_summary)

    # Find variants of the 'jazz' genre
    jazz_variants = get_genre_variants('jazz', artists_df)
    print("\nVariants of 'jazz' genre:")
    print(jazz_variants)
    print("Number of variants:", len(jazz_variants))

    # Summarize the performance of the artist "Michael Jackson"
    summarize_artist_performance("Michael Jackson", artists_df, tracks_df)

if __name__ == "__main__":
    main()
