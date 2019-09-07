{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "dc_listings = pd.read_csv('listings.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3723, 92)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>listing_url</th>\n",
       "      <th>scrape_id</th>\n",
       "      <th>last_scraped</th>\n",
       "      <th>name</th>\n",
       "      <th>summary</th>\n",
       "      <th>space</th>\n",
       "      <th>description</th>\n",
       "      <th>experiences_offered</th>\n",
       "      <th>neighborhood_overview</th>\n",
       "      <th>...</th>\n",
       "      <th>review_scores_value</th>\n",
       "      <th>requires_license</th>\n",
       "      <th>license</th>\n",
       "      <th>jurisdiction_names</th>\n",
       "      <th>instant_bookable</th>\n",
       "      <th>cancellation_policy</th>\n",
       "      <th>require_guest_profile_picture</th>\n",
       "      <th>require_guest_phone_verification</th>\n",
       "      <th>calculated_host_listings_count</th>\n",
       "      <th>reviews_per_month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7087327</td>\n",
       "      <td>https://www.airbnb.com/rooms/7087327</td>\n",
       "      <td>20151002231825</td>\n",
       "      <td>2015-10-03</td>\n",
       "      <td>Historic DC Condo-Walk to Capitol!</td>\n",
       "      <td>Professional pictures coming soon! Welcome to ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Professional pictures coming soon! Welcome to ...</td>\n",
       "      <td>none</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>f</td>\n",
       "      <td>NaN</td>\n",
       "      <td>DISTRICT OF COLUMBIA, WASHINGTON</td>\n",
       "      <td>f</td>\n",
       "      <td>flexible</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>18</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>975833</td>\n",
       "      <td>https://www.airbnb.com/rooms/975833</td>\n",
       "      <td>20151002231825</td>\n",
       "      <td>2015-10-03</td>\n",
       "      <td>Spacious Capitol Hill Townhouse</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Beautifully renovated Capitol Hill townhouse. ...</td>\n",
       "      <td>Beautifully renovated Capitol Hill townhouse. ...</td>\n",
       "      <td>none</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>9.0</td>\n",
       "      <td>f</td>\n",
       "      <td>NaN</td>\n",
       "      <td>DISTRICT OF COLUMBIA, WASHINGTON</td>\n",
       "      <td>f</td>\n",
       "      <td>strict</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>1</td>\n",
       "      <td>2.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8249488</td>\n",
       "      <td>https://www.airbnb.com/rooms/8249488</td>\n",
       "      <td>20151002231825</td>\n",
       "      <td>2015-10-03</td>\n",
       "      <td>Spacious/private room for single</td>\n",
       "      <td>This is an ideal room for a single traveler th...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>This is an ideal room for a single traveler th...</td>\n",
       "      <td>none</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>f</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>f</td>\n",
       "      <td>flexible</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>1</td>\n",
       "      <td>1.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8409022</td>\n",
       "      <td>https://www.airbnb.com/rooms/8409022</td>\n",
       "      <td>20151002231825</td>\n",
       "      <td>2015-10-03</td>\n",
       "      <td>A wonderful bedroom with library</td>\n",
       "      <td>Prime location right on the Potomac River in W...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Prime location right on the Potomac River in W...</td>\n",
       "      <td>none</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>f</td>\n",
       "      <td>NaN</td>\n",
       "      <td>DISTRICT OF COLUMBIA, WASHINGTON</td>\n",
       "      <td>f</td>\n",
       "      <td>flexible</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8411173</td>\n",
       "      <td>https://www.airbnb.com/rooms/8411173</td>\n",
       "      <td>20151002231825</td>\n",
       "      <td>2015-10-03</td>\n",
       "      <td>Downtown Silver Spring</td>\n",
       "      <td>Hi travellers! I live in this peaceful spot, b...</td>\n",
       "      <td>This is a 750 sq ft 1 bedroom 1 bathroom.  Whi...</td>\n",
       "      <td>Hi travellers! I live in this peaceful spot, b...</td>\n",
       "      <td>none</td>\n",
       "      <td>Silver Spring is booming.  You can walk to a n...</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>f</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>f</td>\n",
       "      <td>flexible</td>\n",
       "      <td>f</td>\n",
       "      <td>f</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 92 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        id                           listing_url       scrape_id last_scraped  \\\n",
       "0  7087327  https://www.airbnb.com/rooms/7087327  20151002231825   2015-10-03   \n",
       "1   975833   https://www.airbnb.com/rooms/975833  20151002231825   2015-10-03   \n",
       "2  8249488  https://www.airbnb.com/rooms/8249488  20151002231825   2015-10-03   \n",
       "3  8409022  https://www.airbnb.com/rooms/8409022  20151002231825   2015-10-03   \n",
       "4  8411173  https://www.airbnb.com/rooms/8411173  20151002231825   2015-10-03   \n",
       "\n",
       "                                 name  \\\n",
       "0  Historic DC Condo-Walk to Capitol!   \n",
       "1     Spacious Capitol Hill Townhouse   \n",
       "2    Spacious/private room for single   \n",
       "3    A wonderful bedroom with library   \n",
       "4              Downtown Silver Spring   \n",
       "\n",
       "                                             summary  \\\n",
       "0  Professional pictures coming soon! Welcome to ...   \n",
       "1                                                NaN   \n",
       "2  This is an ideal room for a single traveler th...   \n",
       "3  Prime location right on the Potomac River in W...   \n",
       "4  Hi travellers! I live in this peaceful spot, b...   \n",
       "\n",
       "                                               space  \\\n",
       "0                                                NaN   \n",
       "1  Beautifully renovated Capitol Hill townhouse. ...   \n",
       "2                                                NaN   \n",
       "3                                                NaN   \n",
       "4  This is a 750 sq ft 1 bedroom 1 bathroom.  Whi...   \n",
       "\n",
       "                                         description experiences_offered  \\\n",
       "0  Professional pictures coming soon! Welcome to ...                none   \n",
       "1  Beautifully renovated Capitol Hill townhouse. ...                none   \n",
       "2  This is an ideal room for a single traveler th...                none   \n",
       "3  Prime location right on the Potomac River in W...                none   \n",
       "4  Hi travellers! I live in this peaceful spot, b...                none   \n",
       "\n",
       "                               neighborhood_overview  ... review_scores_value  \\\n",
       "0                                                NaN  ...                 NaN   \n",
       "1                                                NaN  ...                 9.0   \n",
       "2                                                NaN  ...                 NaN   \n",
       "3                                                NaN  ...                 NaN   \n",
       "4  Silver Spring is booming.  You can walk to a n...  ...                 NaN   \n",
       "\n",
       "  requires_license license                jurisdiction_names instant_bookable  \\\n",
       "0                f     NaN  DISTRICT OF COLUMBIA, WASHINGTON                f   \n",
       "1                f     NaN  DISTRICT OF COLUMBIA, WASHINGTON                f   \n",
       "2                f     NaN                               NaN                f   \n",
       "3                f     NaN  DISTRICT OF COLUMBIA, WASHINGTON                f   \n",
       "4                f     NaN                               NaN                f   \n",
       "\n",
       "  cancellation_policy  require_guest_profile_picture  \\\n",
       "0            flexible                              f   \n",
       "1              strict                              f   \n",
       "2            flexible                              f   \n",
       "3            flexible                              f   \n",
       "4            flexible                              f   \n",
       "\n",
       "  require_guest_phone_verification calculated_host_listings_count  \\\n",
       "0                                f                             18   \n",
       "1                                f                              1   \n",
       "2                                f                              1   \n",
       "3                                f                              1   \n",
       "4                                f                              1   \n",
       "\n",
       "  reviews_per_month  \n",
       "0               NaN  \n",
       "1              2.11  \n",
       "2              1.00  \n",
       "3               NaN  \n",
       "4               NaN  \n",
       "\n",
       "[5 rows x 92 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(dc_listings.shape)\n",
    "dc_listings.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3723, 19)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(3723, 19)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "our_acc_value = 3\n",
    "first_living_space_value = dc_listings.loc[0,'accommodates']\n",
    "first_distance = np.abs(first_living_space_value - our_acc_value)\n",
    "print(first_distance)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      461\n",
       "1     2294\n",
       "2      503\n",
       "3      279\n",
       "4       35\n",
       "5       73\n",
       "6       17\n",
       "7       22\n",
       "8        7\n",
       "9       12\n",
       "10       2\n",
       "11       4\n",
       "12       6\n",
       "13       8\n",
       "Name: distance, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dc_listings['distance'] = np.abs(dc_listings.accommodates - our_acc_value)\n",
    "dc_listings.distance.value_counts().sort_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2645     $75.00\n",
       "2825    $120.00\n",
       "2145     $90.00\n",
       "2541     $50.00\n",
       "3349    $105.00\n",
       "Name: price, dtype: object"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dc_listings = dc_listings.sample(frac=1,random_state=0)\n",
    "dc_listings = dc_listings.sort_values('distance')\n",
    "dc_listings.price.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "88.0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dc_listings['price'] = dc_listings.price.str.replace(\"\\$|,\",'').astype(float)\n",
    "mean_price = dc_listings.price.iloc[:5].mean()\n",
    "mean_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "dc_listings.drop('distance',axis=1)\n",
    "train_df = dc_listings.copy().iloc[:2792]\n",
    "test_df = dc_listings.copy().iloc[2792:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict_price(new_listing_value,feature_column):\n",
    "    temp_df = train_df\n",
    "    temp_df['distance'] = np.abs(dc_listings[feature_column] - new_listing_value)\n",
    "    temp_df = temp_df.sort_values('distance')\n",
    "    knn_5 = temp_df.price.iloc[:5]\n",
    "    predicted_price = knn_5.mean()\n",
    "    return(predicted_price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "test_df['predicted_price'] = test_df.accommodates.apply(predict_price,feature_column='accommodates')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "212.98927967051543"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_df['squared_error'] = (test_df['predicted_price'] - test_df['price'])**(2)\n",
    "mse = test_df['squared_error'].mean()\n",
    "rmse = mse ** (1/2)\n",
    "rmse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RMSE for the accommodates column: 212.98927967051543\n",
      "RMSE for the bedrooms column: 216.49048609414763\n",
      "RMSE for the bathrooms column: 216.89419042215684\n",
      "RMSE for the number_of_reviews column: 240.21528314334847\n"
     ]
    }
   ],
   "source": [
    "for feature in ['accommodates','bedrooms','bathrooms','number_of_reviews']:\n",
    "    test_df['predicted_price'] = test_df.accommodates.apply(predict_price,feature_column=feature)\n",
    "    test_df['squared_error'] = (test_df['predicted_price'] - test_df['price'])**(2)\n",
    "    mse = test_df['squared_error'].mean()\n",
    "    rmse = mse ** (1/2)\n",
    "    print(\"RMSE for the {} column: {}\".format(feature,rmse))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "knn = KNeighborsRegressor(algorithm='brute')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
