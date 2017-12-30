# raingDirectorsGenresKeywords

Now, the movies have keywords BUT distributed vertically -not like genres, that makes the movies duplicated (not Unique).
the object now to make keywords distributed horizontally-like genres to have keyword1, keyword2.... features. then we can add these features to the Similarity matrix. 

after cleaning keywords file.. I have combined this with the previous results..


/****** Script for SelectTopNRows command from SSMS  ******/
SELECT R.[id]
--      ,R.[episode_title]
--      ,R.[kind]
      ,R.[rating_rank]
      ,R.[rating_votes]
      ,R.[title]
	  ,D.[directorName]
	  ,K.[column2]
	  ,G.genres_0, G.genres_1,G.genres_2,G.genres_3,G.genres_4,G.genres_5,G.genres_6,G.genres_7,G.genres_8,
	  G.genres_9,G.genres_10,G.genres_11,G.genres_12,G.genres_13,G.genres_14
  FROM [IMBb_Final].[dbo].[ratings] AS R, 
  [IMBb_Final].[dbo].[directors_cleaned_modified3] AS D,
  [IMBb_Final].[dbo].[genres] as G,
  [IMBb_Final].[dbo].[keywords] as K
  WHERE D.movieId = R.id
  AND R.id = G.id
  AND G.id = K.[column1]
  AND R.kind ='movie'
